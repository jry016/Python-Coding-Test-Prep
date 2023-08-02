# LeetCode
# Container With Most Water
# https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_area = 0

        while i <= j:
            hi, hj = height[i], height[j]
            curr_area = min(hi, hj) * (j - i)
            max_area = max(curr_area, max_area)

            if hi > hj:
                j -= 1
            else:
                i += 1
        
        return max_area
        
# Test Case
sol = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(sol.maxArea(height)) # Expected 49