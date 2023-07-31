from typing import List
from collections import deque

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_q = deque(nums)
        zeros = []
        nums.clear()
        while nums_q:
            curr = nums_q.popleft()
            if curr == 0:
                zeros.append(curr)
            
            else:
                nums.append(curr)

        nums.extend(zeros)
# Test Cases
sol = Solution()
nums = [0,1,0,3,12]
sol.moveZeroes([0,1,0,3,12])
print(nums)