from collections import Counter

d = {"a": 5, "b": 3, "c": 5, "d": 1}

people = {"Alice": 25.004, "Bob": 30, "Charlie": 35}
print(f"people: #{", #".join(people.keys())}")
      
print(format(people["Alice"],".2f"))
sorted_people = sorted(people.items(), key=lambda x: x[1], reverse=True)
print(sorted_people)

top_2 = Counter(d).most_common(2)
print(top_2)


# transactions = [
#     ("Vida", 650),
#     ("Vida", 720),   # ← first to exceed 700
#     ("John", 800),
# ]

transactions = [("Vida",720), ("Alice",650), ("John",800)]

scores = {}
first_qualified = None

for name, score in transactions:
    scores[name] = max(scores.get(name, 0), score)  # keep running max
    if scores[name] > 700 and first_qualified is None:
        first_qualified = name

print(first_qualified, scores)
matrix = [[0]*i for i in range(3)]
print(matrix)