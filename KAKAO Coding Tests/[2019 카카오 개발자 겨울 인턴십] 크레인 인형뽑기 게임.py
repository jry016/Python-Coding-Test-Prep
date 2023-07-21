# 2019 카카오 개발자 겨울 인턴십
# 크레인 인형 뽑기 게임
# https://school.programmers.co.kr/learn/courses/30/lessons/64061

def reshape(arr):
    reshaped_arr = list(zip(*arr)) # (zip(*arr)) transposes 2D array
                                   # *arr unpacks rows of the array and zip takes these arguments 
                                   # and pairs up the corresponding elements as tuples
    
    reshaped = [list(inner_tuple) for inner_tuple in reshaped_arr]
    return reshaped

def solution(board, moves):
    answer = 0
    board = reshape(board) # transpose the board
    result = []
                
    for i in moves:
        for j in range(len(board)):
            if(board[i-1][j] != 0):
                result.append(board[i-1][j])
                board[i-1][j] = 0

                if len(result) > 1:
                    if(result[-1] == result[-2]):
                        answer += 2
                        result = result[:-2]
                break
    # Solution without Transposing the Board
    # for i in moves:
    #     for j in range(len(board)):
    #         if(board[j][i-1] != 0):
    #             result.append(board[j][i-1])
    #             board[j][i-1] = 0

    #             if len(result) > 1:
    #                 if(result[-1] == result[-2]):
    #                     answer += 2
    #                     result = result[:-2]
    #             break
        
    return answer

# Test Case
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
result = solution(board, moves)
print(f"Result of Board Moves: {result}")