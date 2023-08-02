# LeetCode
# Kids With the Greatest Number of Candies
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        candy_max = max(candies)
        isMax = []
        for i in candies:
            if i + extraCandies >= candy_max:
                isMax.append(True)
            else:
                isMax.append(False)

        return isMax

# Test Cases
candies1 = [2,3,5,1,3]
extraCandies1 = 3

candies2 = [4,2,1,1,2]
extraCandies2 = 1

candies3 = [12,1,12]
extraCandies3 = 10

sol = Solution()
print(sol.kidsWithCandies(candies1, extraCandies1))
print(sol.kidsWithCandies(candies2, extraCandies2))
print(sol.kidsWithCandies(candies3, extraCandies3))