# Two pointers
# Example: 1. 3Sum
# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
# Note: The solution set must not contain duplicate triplets.

# Example:
# Input: nums = [-1, 0, 1, 2, -1, -4]
# Output: [[-1, -1, 2], [-1, 0, 1]]
# Explanation: There are two triplets which gives the sum of zero.

# Solution:
# 1. Sort the array.
# 2. Iterate through the array.
# 3. For each element, use two pointers to find the sum of the remaining elements.
# 4. If the sum is less than zero, increment the left pointer.
# 5. If the sum is greater than zero, decrement the right pointer.
# 6. If the sum is equal to zero, add it to the result.
# 7. Skip the duplicates.
# 8. Return the result.

def three_sum(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return result

# Time complexity: O(n^2)
# Space complexity: O(1)

print(three_sum([-1, 0, 1, 2, -1, -4]))  # [[-1, -1, 2], [-1, 0, 1]]