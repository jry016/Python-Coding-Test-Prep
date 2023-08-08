# LeetCode
# Maximum Average Subarray I
# https://leetcode.com/problems/maximum-average-subarray-i/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])  
        max_average = window_sum / k  

        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]  
            max_average = max(max_average, window_sum / k) 
        
        return float(max_average)

# Test Cases
sol = Solution()
nums = [1,12,-5,-6,50,3]
k = 4
print(sol.findMaxAverage(nums, k))

nums = [5]
k = 1
print(sol.findMaxAverage(nums, k))

# Attempt 1 -- Exceeded Time Limit
# class Solution:
#     def findMaxAverage(self, nums: List[int], k: int) -> float:
#         curr_avg = float('-inf')
#         i = 0

#         while i <= len(nums) - k:
#             avg = sum(nums[i:i+k]) / k

#             if avg > curr_avg:
#                 curr_avg = avg
#             i += 1
        
#         return float(curr_avg)
