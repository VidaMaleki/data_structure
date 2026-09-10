from flask import Flask, request, jsonify

app = Flask(__name__)

# ─────────────────────────────────────────
# fake database
# ─────────────────────────────────────────
loans_db = {}
next_id = 1

# ─────────────────────────────────────────
# helper functions
# ─────────────────────────────────────────
def validate_loan_input(data):
    """validate input for creating a loan"""
    if not data:
        return "Request body is missing"
    if "amount" not in data:
        return "amount is required"
    if "applicant_name" not in data:
        return "applicant_name is required"
    if not isinstance(data["amount"], (int, float)):
        return "amount must be a number"
    if data["amount"] <= 0:
        return "amount must be greater than 0"
    if not isinstance(data["applicant_name"], str):
        return "applicant_name must be a string"
    if not data["applicant_name"].strip():
        return "applicant_name cannot be empty"
    return None

def find_loan(loan_id):
    """find loan by id, return None if not found"""
    return loans_db.get(loan_id)

# ─────────────────────────────────────────
# GET all loans
# ─────────────────────────────────────────
@app.route("/loans", methods=["GET"])
def get_all_loans():
    """
    GET /loans
    returns all loans
    200 — success (even if empty)
    """
    try:
        loans = list(loans_db.values())
        return jsonify({
            "loans": loans,
            "total": len(loans)        # bonus — tell caller how many
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ─────────────────────────────────────────
# GET one loan
# ─────────────────────────────────────────
@app.route("/loans/<int:loan_id>", methods=["GET"])
def get_loan(loan_id):
    """
    GET /loans/<id>
    returns single loan
    200 — found
    404 — not found
    """
    try:
        loan = find_loan(loan_id)
        if not loan:
            return jsonify({"error": f"Loan {loan_id} not found"}), 404
        return jsonify(loan), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ─────────────────────────────────────────
# POST create loan
# ─────────────────────────────────────────
@app.route("/loans", methods=["POST"])
def create_loan():
    """
    POST /loans
    creates a new loan
    201 — created
    400 — invalid input
    """
    global next_id
    try:
        data = request.get_json()

        error = validate_loan_input(data)
        if error:
            return jsonify({"error": error}), 400

        loan = {
            "id": next_id,
            "amount": data["amount"],
            "applicant_name": data["applicant_name"].strip(),
            "status": "pending"        # default status
        }
        loans_db[next_id] = loan
        next_id += 1

        return jsonify(loan), 201      # 201 = created ✅

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ─────────────────────────────────────────
# PUT update loan
# ─────────────────────────────────────────
@app.route("/loans/<int:loan_id>", methods=["PUT"])
def update_loan(loan_id):
    """
    PUT /loans/<id>
    updates existing loan
    200 — updated
    400 — invalid input
    404 — not found
    """
    try:
        loan = find_loan(loan_id)
        if not loan:
            return jsonify({"error": f"Loan {loan_id} not found"}), 404

        data = request.get_json()
        if not data:
            return jsonify({"error": "Request body is missing"}), 400

        # only allow updating certain fields
        allowed_fields = {"amount", "applicant_name", "status"}
        invalid_fields = set(data.keys()) - allowed_fields
        if invalid_fields:
            return jsonify({
                "error": f"Invalid fields: {invalid_fields}"
            }), 400

        # validate status if provided
        valid_statuses = {"pending", "approved", "rejected"}
        if "status" in data and data["status"] not in valid_statuses:
            return jsonify({
                "error": f"status must be one of {valid_statuses}"
            }), 400

        # validate amount if provided
        if "amount" in data and data["amount"] <= 0:
            return jsonify({
                "error": "amount must be greater than 0"
            }), 400

        # update only provided fields
        loan.update(data)
        return jsonify(loan), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ─────────────────────────────────────────
# PATCH partial update
# ─────────────────────────────────────────
@app.route("/loans/<int:loan_id>", methods=["PATCH"])
def patch_loan(loan_id):
    """
    PATCH /loans/<id>
    partially updates a loan (e.g. just status)
    same as PUT but semantically for partial updates
    200 — updated
    404 — not found
    """
    try:
        loan = find_loan(loan_id)
        if not loan:
            return jsonify({"error": f"Loan {loan_id} not found"}), 404

        data = request.get_json()
        if not data:
            return jsonify({"error": "Request body is missing"}), 400

        # update only fields that were sent
        for key, value in data.items():
            if key in loan:            # only update existing fields
                loan[key] = value

        return jsonify(loan), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ─────────────────────────────────────────
# DELETE one loan
# ─────────────────────────────────────────
@app.route("/loans/<int:loan_id>", methods=["DELETE"])
def delete_loan(loan_id):
    """
    DELETE /loans/<id>
    deletes a loan
    200 — deleted
    404 — not found
    """
    try:
        loan = find_loan(loan_id)
        if not loan:
            return jsonify({"error": f"Loan {loan_id} not found"}), 404

        del loans_db[loan_id]
        return jsonify({
            "message": "Loan deleted successfully",
            "loan": loan
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ─────────────────────────────────────────
# DELETE all loans
# ─────────────────────────────────────────
@app.route("/loans", methods=["DELETE"])
def delete_all_loans():
    """
    DELETE /loans
    deletes all loans
    200 — deleted
    """
    try:
        count = len(loans_db)
        loans_db.clear()
        return jsonify({
            "message": f"{count} loans deleted successfully"
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ─────────────────────────────────────────
# GET loans with filtering
# ─────────────────────────────────────────
@app.route("/loans/search", methods=["GET"])
def search_loans():
    """
    GET /loans/search?status=approved&min_amount=1000
    filters loans by query params
    200 — success
    """
    try:
        status = request.args.get("status")
        min_amount = request.args.get("min_amount", type=float)
        max_amount = request.args.get("max_amount", type=float)

        loans = list(loans_db.values())

        # apply filters
        if status:
            loans = [l for l in loans if l["status"] == status]
        if min_amount:
            loans = [l for l in loans if l["amount"] >= min_amount]
        if max_amount:
            loans = [l for l in loans if l["amount"] <= max_amount]

        return jsonify({
            "loans": loans,
            "total": len(loans)
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ─────────────────────────────────────────
# test without flask
# ─────────────────────────────────────────
if __name__ == "__main__":
    # app.run(debug=True)

    # simulate create
    loans_db[1] = {"id": 1, "amount": 1000, "applicant_name": "Vida", "status": "pending"}
    loans_db[2] = {"id": 2, "amount": 5000, "applicant_name": "John", "status": "approved"}
    next_id = 3

    print("all loans:", list(loans_db.values()))
    print("loan 1:", find_loan(1))
    print("loan 99:", find_loan(99))