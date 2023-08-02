# LeetCode
# Is Subsequence
# https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=leetcode-75

from collections import deque

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        str1 = deque(s)
        t = deque(t)
        strf = ''

        while t:
            if str1 and str1[0] == t[0]:
                strf += t.popleft()
                str1.popleft()
            else:
                t.popleft()

        return strf == s

# Test Cases
sol = Solution()
s = "abc"
t = "ahbgdc"
print(sol.isSubsequence(s, t)) # Expected Output: True

s = "axc"
t = "ahbgdc"
print(sol.isSubsequence(s, t)) # Expected Output: False
