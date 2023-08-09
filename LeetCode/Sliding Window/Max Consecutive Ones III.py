# LeetCode
# Max Consecutive Ones III
# https://leetcode.com/problems/max-consecutive-ones-iii/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        curr_max = 0

        while right < len(nums):
            if nums[right] == 0:
                if k > 0:
                    k -= 1
                else:
                    curr_max = max(curr_max, right - left)
                    while nums[left] != 0:
                        left += 1
                    left += 1
                    
            right += 1
        if k >= 0:
            curr_max = max(curr_max, right - left)

        return curr_max
    
# Test Cases
sol = Solution()
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(sol.longestOnes(nums, k)) # Expected Output 6

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
print(sol.longestOnes(nums, k)) # Expected Output 10

nums = [0,0,0,1]
k = 4
print(sol.longestOnes(nums, k)) # Expected Output 4

# Alternative Solutionclass Solution:
    # def longestOnes(self, A: List[int], K: int) -> int:
    #   left = right = 0
      
    #   for right in range(len(A)):
    #     # if we encounter a 0 the we decrement K
    #     if A[right] == 0:
    #       K -= 1
    #     # else no impact to K
        
    #     # if K < 0 then we need to move the left part of the window forward
    #     # to try and remove the extra 0's
    #     if K < 0:
    #       # if the left one was zero then we adjust K
    #       if A[left] == 0:
    #         K += 1
    #       # regardless of whether we had a 1 or a 0 we can move left side by 1
    #       # if we keep seeing 1's the window still keeps moving as-is
    #       left += 1
      
    #   return right - left + 1