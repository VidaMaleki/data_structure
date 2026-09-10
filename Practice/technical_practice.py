log_a = [
    "2025-01-01,Store,uuid1,100",
    "2025-01-01,Web,uuid2,500",
    "2025-01-02,Store,uuid1,200",
]

log_b = [
    "2025-01-02,Phone,uuid2,100",
    "2025-01-02,Store,uuid3,800",
    "2025-01-01,Web,uuid1,50",
]

# Expected output:
# uuid3 spent $800 ← most
# return ["uuid3"]

# tie example:
# if uuid1 total = uuid2 total → return ["uuid1", "uuid2"]
# Find the user who spent the most money.
# If tie → return both users.

# Return: user_id(s)

def most_spent_user(log_a, log_b):
    user_balance = {}
    for transaction in log_a + log_b:
        date, bill, user_id, amount = transaction.split(",")
        
        user_balance[user_id] = user_balance.get(user_id, 0) + int(amount)
    
    max_spent = max(user_balance.values())
    return [user for user, spent in user_balance.items() if spent == max_spent]
    
print(most_spent_user(log_a, log_b))   

"""
Given a list of transactions, find any users 
who made transactions on 3 or more different days.

Input:
transactions = [
    "2025-01-01,Store,uuid1,100",
    "2025-01-02,Store,uuid1,200",
    "2025-01-03,Web,uuid1,50",
    "2025-01-01,Web,uuid2,500",
    "2025-01-02,Store,uuid2,100",
    "2025-01-01,Store,uuid3,800",
]

Output: ["uuid1"]
# uuid1 → 3 different days ✅
# uuid2 → 2 different days ❌
# uuid3 → 1 day ❌
"""



def user_with_most_days(transactions):
    users_day = {}
    for transaction in transactions:
        date, cost_type, user_id, amount = transaction.split(",")
        users_day.setdefault(user_id, set()).add(date)
    
    top_users = [user for user, date in users_day.items() if len(date)>= 3]
    return top_users

# print(user_with_most_days(transactions))

"""
Given a list of transactions, return a 
summary string for each user in this format:

"uuid1: $350 across 3 transactions"

Input:
transactions = [
    "2025-01-01,Store,uuid1,100",
    "2025-01-02,Web,uuid1,200",
    "2025-01-03,Store,uuid1,50",
    "2025-01-01,Web,uuid2,500",
    "2025-01-02,Store,uuid2,100",
]

Output:
[
    "uuid1: $350 across 3 transactions",
    "uuid2: $600 across 2 transactions"
]

Results should be sorted alphabetically by user_id.
"""

transactions = [
    "2025-01-01,Store,uuid1,100",
    "2025-01-02,Web,uuid1,200",
    "2025-01-03,Store,uuid1,50",
    "2025-01-01,Web,uuid2,500",
    "2025-01-02,Store,uuid2,100",
]

def transaction_history(transactions):
    user_transactions = {}
    user_days = {}
    for transaction in transactions:
        date, cost_type, user_id, amount = transaction.split(",")
        user_transactions[user_id] = user_transactions.get(user_id, 0) + int(amount)
        user_days.setdefault(user_id, set()).add(date)
        
    
    result = []
    for user, value in user_days.items():
        days = len(value)
        cost = user_transactions[user]
        result.append(f'{user}: ${cost} across {days} transactions')
    return sorted(result)

print(transaction_history(transactions))

"""
Given transactions find the maximum total 
spent in any 3 consecutive transactions
"""
def maxConsecutiveSpend(transactions):
    amounts = [int(t.split(",")[3]) for t in transactions]
    print("amount:" , amounts)
    window_sum = sum(amounts[:3])
    max_sum = window_sum
    
    for i in range(3, len(amounts)):
        window_sum += amounts[i] - amounts[i-3]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

print(maxConsecutiveSpend(transactions))

days = [t.split(",")[0] for t in transactions]
print("days:" , days)