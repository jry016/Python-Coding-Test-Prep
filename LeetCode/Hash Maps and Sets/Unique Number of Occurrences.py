# LeetCode
# Unique Number of Occurrences
# https://leetcode.com/problems/unique-number-of-occurrences/?envType=study-plan-v2&envId=leetcode-75

from typing import List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrence = {}

        for i in arr:
            if i in occurrence:
                occurrence[i] += 1
            else:
                occurrence[i] = 1
        
        seen_values = set()
        for value in occurrence.values():
            if value in seen_values:
                return False
            seen_values.add(value)
        
        return True

# Test Cases
sol = Solution()
arr = [1,2,2,1,1,3]
print(sol.uniqueOccurrences(arr)) # True

arr = [1,2]
print(sol.uniqueOccurrences(arr)) # False

arr = [-3,0,1,-3,1,1,1,-3,10,0]
print(sol.uniqueOccurrences(arr)) # True