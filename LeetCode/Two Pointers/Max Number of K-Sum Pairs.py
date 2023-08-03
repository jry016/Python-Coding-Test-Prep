# LeetCode
# Max Number of K-Sum Pairs
# https://leetcode.com/problems/max-number-of-k-sum-pairs/

from typing import List

# Two pointer approach
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        nums.sort()
        i = 0
        j = len(nums) - 1

        while i < j:
            curr = nums[i] + nums[j]
            if curr == k:
                count += 1
                i += 1
                j -= 1
            elif curr > k:
                j -= 1
            else:
                i += 1

        return count
    
# Test Cases
sol = Solution()
nums = [1,2,3,4] 
k = 5
print(sol.maxOperations(nums, k)) # Expected: 2

nums = [3,1,3,4,3]
k = 6
print(sol.maxOperations(nums, k)) # Expected: 1

# class Solution:
#     def maxOperations(self, nums: List[int], k: int) -> int:
#         num_freq = {}  # Dictionary to store the frequency of each number
#         count = 0

#         for num in nums:
#             complement = k - num  # The number needed to sum up to k
#             if complement in num_freq and num_freq[complement] > 0:
#                 count += 1
#                 num_freq[complement] -= 1
#             else:
#                 num_freq[num] = num_freq.get(num, 0) + 1

#         return count