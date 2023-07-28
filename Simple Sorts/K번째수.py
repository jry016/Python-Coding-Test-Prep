# K번째수
# https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    for command in commands:
        arr = array.copy()
        arr = arr[command[0]-1: command[1]]
        arr.sort()
        answer.append(arr[command[2]-1])
        
    return answer

# Test Cases:
arr = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(arr, commands)) # [5, 6, 3]

# Alternative:

# def solution(array, commands):
#     answer = []
#     for command in commands:
#         i,j,k = command
#         answer.append(list(sorted(array[i-1:j]))[k-1])
#     return answer