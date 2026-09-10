# Given a list of numbers, sort them 
# without using the built-in sort() method
# Implement bubble sort

# Input:  [64, 34, 25, 12, 22, 11, 90]
# Output: [11, 12, 22, 25, 34, 64, 90]
s = [64, 34, 25, 12, 22, 11, 90, 11]
def bubble_sort(nums: list) -> list:
    for i in range(len(nums)):
        for j in range(len(nums)-1-i):
            
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                
    return nums

# print(bubble_sort(s))


ss="hello world hello"
# print("hello".count("l"))
nums_dict = {}
for num in s:
    nums_dict[num] = nums_dict.setdefault(num, 0)+1
# print(nums_dict)

users = {
    "Vida":  {"credit_score": 750, "income": 60000},
    "John":  {"credit_score": 650, "income": 80000},
    "Alice": {"credit_score": 800, "income": 90000},
    "Bob":   {"credit_score": 720, "income": 55000}
}

eligible = {k:v for k,v in users.items() if v["credit_score"] >= 750}
max_income_user = max(eligible, key=lambda k: eligible[k]["income"])
print(max_income_user)

d = {"b": 2, "a": 1, "c": 3}
a = {"b": 2, "k": 1, "p": 3}
print(d | a)

from collections import defaultdict
d = defaultdict(list)
print(d)