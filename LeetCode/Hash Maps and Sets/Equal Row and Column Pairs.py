# LeetCode
# Equal Row and Column Pairs
# https://leetcode.com/problems/equal-row-and-column-pairs/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cnt = 0
        for row in range(len(grid)):
            for col in range(len(grid)):
                if grid[row] == [grid[i][col] for i in range(len(grid))]:
                    cnt += 1
        return cnt

# Test Cases
sol = Solution()
grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
print(sol.equalPairs(grid)) # 3

grid = [[3,2,1],[1,7,6],[2,7,7]]
print(sol.equalPairs(grid)) # 1

# *** Saving Columns ***
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(len(matrix[0]))
# columns = [[] for _ in range(len(matrix[0]))]
# for row in matrix:
#     print(f"Current Row: {row}")
#     for col_idx, value in enumerate(row):
#         print(f"Current Col Idx: {col_idx} and Value: {value}")
#         columns[col_idx].append(value)
#         print(columns)
# print("Final Columns: ", columns)

