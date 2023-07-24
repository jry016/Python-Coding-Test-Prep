# 2018 KAKAO BLIND RECRUITMENT
# [1차] 프렌즈4블록
# https://school.programmers.co.kr/learn/courses/30/lessons/17679

from collections import deque

def check_board(board, m, n):
    remove_set = set()
    for i in range(m - 1):  # Fix 1: Iterate up to m-1
        for j in range(n - 1):
            # board condition to check for 2x2 tile
            if (board[i][j] == board[i][j + 1] == board[i + 1][j] == board[i + 1][j + 1]) and board[i][j] != '0':
                # Add positions of 2x2 tiles with the same element to remove_set
                remove_set.add((i, j))
                remove_set.add((i, j + 1))
                remove_set.add((i + 1, j))
                remove_set.add((i + 1, j + 1))
    return remove_set

def rearrange_board(board, m, n, remove_set):
    for i, j in remove_set:
        board[i][j] = '0'
    
    # Iterate over columns
    for j in range(n): 
        zero_positions = deque([])
        
        # Iterate from the bottom row to top
        for i in range(m - 1, -1, -1):
            # Keep track of all 0 positions in deque
            if board[i][j] == '0':
                zero_positions.append((i, j))
                
            else:   # If character is position is non-zero
                if zero_positions: # if zero_positions is not empty
                    # Swap 0 in (i, j) and character coordinates(qi, qj)
                    qi, qj = zero_positions.popleft()
                    board[qi][qj] = board[i][j]
                    board[i][j] = '0'
                    zero_positions.append((i, j)) # add current position back for future swaps 
                                                  # in the same column
    return board

def solution(m, n, board):
    total = 0
    board = [list(i) for i in board]
    remove_set = set()
    
    while True:
        remove_set = check_board(board, m, n)
        if remove_set:
            total += len(remove_set)
            board = rearrange_board(board, m, n, remove_set)
            remove_set.clear()  
            
        else:
            break
        
    return total

# Test Cases:
m1, n1 = 4, 5
m2, n2 = 6, 6
board1 = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
board2 = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]

print(solution(m1, n1, board1))  # Expected Output = 14
print(solution(m2, n2, board2))  # Expected Output = 15

### Approach 1: 
# def split_input(board):
#     new_board = []
#     for item in board:
#         new_board.append(list(item))
#     return new_board

# def unique_elements(m, n, board):
#     unique = []
#     for i in range(m):
#         for j in range(n):
#             if board[i][j] not in unique:
#                 unique.append(board[i][j])
#     return unique

# def createTiles(unique_block):
#     tiles = []
#     for alphabet in unique_block:
#         tiles.append([[alphabet, alphabet], [alphabet, alphabet]])
#     return tiles

# def solution(m, n, board):
#     total = 0
#     board = split_input(board) # alternative: [list(i) for i in board]
#     unique_block = unique_elements(m, n, board)
    
#     # List of 2 by 2 Tiles
#     tiles = createTiles(unique_block)
    
#     for tile in tiles:
#         for i in range(m-1):
#             for j in range(n-1):
#                 match = True
#                 for x in range(2):
#                     for y in range(2):
#                         if tile[x][y] != board[x+i][y+j]:
#                             match = False
#                             break
#                     if not match:
#                         break
#                 if match:
                    
#     return total