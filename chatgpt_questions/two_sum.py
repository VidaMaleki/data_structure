"""
Problem:
Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.

Assumptions:

Each input has exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Example:

plaintext
Copy code
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Hints:

Try solving this with a brute-force approach first, then think about how you could make it more efficient.
After solving, review the time complexity of your solution.
"""
nums = [2, 11, 15, 7]
target = 9
def two_sum(nums, target):
    answer = {}
    
    for i, num in enumerate(nums):
        temp = target - num
        if temp in answer:
            if i != answer[temp]:
                return [answer[temp], i]
        answer[num] = i
    return []

print(two_sum(nums, target))  # [0, 1]