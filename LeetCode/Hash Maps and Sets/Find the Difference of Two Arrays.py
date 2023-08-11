# LeetCode
# Find the Difference of Two Arrays
# https://leetcode.com/problems/find-the-difference-of-two-arrays/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1, nums2 = set(nums1), set(nums2)
        unique_nums1 = nums1 - nums2
        unique_nums2 = nums2 - nums1

        answer = [list(unique_nums1), list(unique_nums2)]
        return answer
        

# Test Cases
sol = Solution()
nums1 = [1,2,3]
nums2 = [2,4,6]
print(sol.findDifference(nums1, nums2)) # [[1,3],[4,6]]

nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
print(sol.findDifference(nums1, nums2)) # [[3],[]]

