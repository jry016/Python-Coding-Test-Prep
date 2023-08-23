# LeetCode
# Longest Subarray of 1's After Deleting One Element
# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, right, k = 0, 0, 1
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
        
        return right - left
    
# Test Cases
sol = Solution()
nums = [1,1,0,1]
print(sol.longestSubarray(nums)) # Output: 3

nums = [0,1,1,1,0,1,1,0,1]
print(sol.longestSubarray(nums)) # Output: 5

nums = [1,1,1]
print(sol.longestSubarray(nums)) # Output: 2