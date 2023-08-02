# LeetCode
# Can Place Flowers
# https://leetcode.com/problems/can-place-flowers/?envType=study-plan-v2&envId=leetcode-75

from typing import List
from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while i < len(flowerbed) and n > 0:
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0):
                if i == len(flowerbed) - 1 or flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
            i += 1

        return n == 0

# Test Cases
flowerbed1 = [1,0,0,0,1]
n1 = 1

flowerbed2 = [1,0,0,0,1]
n2 = 2

flowerbed3 = [1,0,0,0,0,1]
n3 = 2

sol = Solution()
print(sol.canPlaceFlowers(flowerbed1, n1)) # True
print(sol.canPlaceFlowers(flowerbed2, n2)) # False
print(sol.canPlaceFlowers(flowerbed3, n3)) # False

# Attempt 2
# from typing import List

# class Solution:
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         i = 0
#         while i < len(flowerbed) and n > 0:
#             if flowerbed[i] == 0:
#                 # Base Case i == 0
#                 if i == 0 or flowerbed[i - 1] == 0:  # Check left adjacent
#                     if i == len(flowerbed) - 1 or flowerbed[i + 1] == 0:  # Check right adjacent
#                         flowerbed[i] = 1  # Plant flower
#                         n -= 1  # Decrement the count of remaining flowers to be planted
#             i += 1

#         return n == 0