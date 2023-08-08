# LeetCode
# Maximum Number of Vowels in a Substring of Given Length
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_cnt, curr_cnt = 0, 0
        s = list(s)
        vowels = set('aeiouAEIOU') 

        # Base Case
        for i in range(k):
            if s[i] in vowels:
                curr_cnt += 1
        max_cnt = curr_cnt

        for i in range(k, len(s)):
            if s[i - k] in vowels:  # Remove the leftmost character from the window
                curr_cnt -= 1
            if s[i] in vowels:  # Add the new character to the window
                curr_cnt += 1
            max_cnt = max(max_cnt, curr_cnt)  # Update max_cnt
        
        return max_cnt
    
# Test Cases
sol = Solution()
s = "abciiidef"
k = 3
print(sol.maxVowels(s, k)) # Expected Output = 3

s = "aeiou"
k = 2
print(sol.maxVowels(s, k)) # Expected Output = 2

s = "leetcode"
k = 3
print(sol.maxVowels(s, k)) # Expected Output = 2


            
            
            
