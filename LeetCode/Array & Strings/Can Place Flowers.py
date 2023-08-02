# LeetCode
# Can Place Flowers
# https://leetcode.com/problems/can-place-flowers/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        count = 0
        for i in flowerbed:
            if i == 0:
                count += 1
        
        if count >= n:
            return True
        else:
            return False

# Test Cases
flowerbed1 = [1,0,0,0,1]
n1 = 1

flowerbed2 = [1,0,0,0,1]
n2 = 2

sol = Solution()
print(sol.canPlaceFlowers(flowerbed1, n1))
print(sol.canPlaceFlowers(flowerbed2, n2))