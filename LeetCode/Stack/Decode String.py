# LeetCode
# Decode String
# https://leetcode.com/problems/decode-string/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        curr_num = 0

        str_stack = []
        curr_string = ''
        
        for char in s:
            if char.isdigit():
                curr_num = curr_num * 10 + int(char) # Incase the number is a multi-digit

            elif char == '[':
                num_stack.append(curr_num)
                curr_num = 0

                str_stack.append(curr_string)
                curr_string = ''
            
            elif char == ']':
                curr_string = str_stack.pop() + curr_string * num_stack.pop()
            
            elif char.isalpha():
                curr_string += char

        return curr_string
            

# Test Cases
sol = Solution()
s = "3[a]2[bc]"
print(sol.decodeString(s)) # Expected Output: "aaabcbc"

s = "3[a2[c]]"
print(sol.decodeString(s)) # Expected Output: "accaccacc"

s = "2[abc]3[cd]ef"
print(sol.decodeString(s)) # Expected Output: "abcabccdcdcdef"

# Rough Attempt 1
# class Solution:
#     def decodeString(self, s: str) -> str:
#         stack = []
#         copy = ''
#         for char in s:
#             if char.isdigit():
#                 stack.append(int(char))
#             elif char == '[':
#                 while char != ']':
#                     copy += char
#                 copy = stack[-1] * copy
#                 stack.pop()
#                 stack.append(copy)
#                 copy = ''

#             elif char.isalpha():
#                 stack.append(char)
        
#         return str(stack)
            