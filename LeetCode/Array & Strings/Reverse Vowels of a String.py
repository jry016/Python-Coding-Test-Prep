
class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        vowels = set('aeiouAEIOU') # Faster Runtime
        #vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        i = 0
        j = len(s) - 1

        while i < j:
            if s_list[i] in vowels and s_list[j] in vowels:
                s_list[i], s_list[j] = s_list[j], s_list[i]
                i += 1
                j -= 1
            
            elif s_list[i] in vowels and s_list[j] not in vowels:
                j -= 1

            elif s_list[i] not in vowels and s_list[j] in vowels:
                i += 1

            else:
                i += 1
                j -= 1
        
        return ''.join(s_list)
    
# Test Cases
sol = Solution()
s = "hello"
print(sol.reverseVowels(s))
            
