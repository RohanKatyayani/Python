"""
Problem Statement (LeetCode #1): -
Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.
	•	You may assume each input has exactly one solution.
	•	You cannot use the same element twice.
"""

# Todo: Step 1 - Brute Force Approach
"""
Loop through every pair(i, j), check if nums[i] + nums[j] == target, Time complexity = O(n²). Not optimal for large inputs. 
"""

def two_sum_brute(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n): # Don't repeat the same element
            if nums[i] + nums[j] == target:
                return [i, j]

# Todo: Step 2 - HashMap (Optimal Solution)
"""
Solve in O(n) using a dictionary. As we scan the Array, we subtract the first element from the target. Then we store the 
first element in the dictionary. Once that is done, we subtract the second element from the target and compare if the 
complement is something we already have, if we do, that's our answer, if we don't, we go to the next element(num).  
"""

def two_sum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i

# Todo: Step 3 - Implementation

nums = [2, 7, 11, 15]
target = 9

print("Brute Force:", two_sum_brute(nums, target))    # [0, 1]
print("HashMap Optimal:", two_sum(nums, target))      # [0, 1]

nums2 = [3, 2, 4]
target2 = 6
print("Brute Force:", two_sum_brute(nums2, target2))  # [1, 2]
print("HashMap Optimal:", two_sum(nums2, target2))    # [1, 2]


