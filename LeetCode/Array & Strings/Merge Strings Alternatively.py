# LeetCode
# Merge Strings Alternatively
# https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def mergeAlternatively(self, word1: str, word2: str) -> str:
        merged = []
        i, j = 0, 0

        if len(word1) != len(word2):
            if len(word1) > len(word2):
                while len(word1) != len(word2):
                    word2 = word2 + ' '
            else:
                while len(word1) != len(word2):
                    word1 = word1 + ' '

        while i < len(word1) and j < len(word2):
            merged.append(word1[i])
            merged.append(' ')
            merged.append(word2[j])
            merged.append(' ')
            i += 1
            j += 1


        result = ''.join(merged)
        return result

# Test Cases
sol = Solution()
print(sol.mergeAlternatively("abc", "pqr"))
print(sol.mergeAlternatively("ab", "pqrs"))
print(sol.mergeAlternatively("abcd", "pq"))
