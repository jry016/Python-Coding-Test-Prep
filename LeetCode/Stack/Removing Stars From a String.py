from collections import deque

class Solution:
    def removeStars(self, s: str) -> str:
        d = deque()
        for char in s:
            if char == '*':
                if d:
                    d.pop()
            else:
                d.append(char)
        return ''.join(d)

# Test Cases
s = "leet**cod*e"
sol = Solution()
print(sol.removeStars(s))

# s_list = list(s)
# stack = []
# for char in s_list:
#     if char == '*':
#         if stack:
#             stack.pop()
#     else:
#         stack.append(char)
# print(stack)