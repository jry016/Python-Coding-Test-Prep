# LeetCode
# Find the Highest Altitude
# https://leetcode.com/problems/find-the-highest-altitude/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0]
        curr_alt = 0
        for i in gain:
            curr_alt += i
            altitudes.append(curr_alt)

        return max(altitudes)

# Test Cases
sol = Solution()
gain = [-5,1,5,0,-7]
print(sol.largestAltitude(gain)) # Expected Output = 1

gain = [-4,-3,-2,-1,4,3,2]
print(sol.largestAltitude(gain)) # Expected Output = 0