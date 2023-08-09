# LeetCode
# Find Pivot Index
# https://leetcode.com/problems/find-pivot-index/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0

        for i in range(0, len(nums)):
            if left_sum * 2 == total_sum - nums[i]:
                return i
            left_sum += nums[i]

        return -1
    
# Test Case
sol = Solution()
nums = [1,7,3,6,5,6] # 28
print(sol.pivotIndex(nums)) # Expected Output: 3

nums = [1,2,3]
print(sol.pivotIndex(nums)) # Expected Output: -1

nums = [2,1,-1]
print(sol.pivotIndex(nums)) # Expected Output: 0

nums = [-1,-1,-1,0,1,1]
print(sol.pivotIndex(nums)) # Expected Output: 0

nums = [-1,-1,0,1,1,0]
print(sol.pivotIndex(nums)) # Expected Output: 5