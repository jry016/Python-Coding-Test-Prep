# 연습문제
# 하노이의 탑
# https://school.programmers.co.kr/learn/courses/30/lessons/12946

# Solving Recursive Problems
# Let f(n) be a recursive function
# 1. Identify f(1) Base Case
# 2. Assume f(n-1) works
# 3. Show f(n) works using f(n-1)

def hanoi(n, start, end):
    moves = []
    if n == 1:
        return [[start, end]]
    
    else: 
        mid = 6 - (start + end)
        moves += hanoi(n-1, start, mid)
        moves.append([start, end])
        moves += hanoi(n-1, mid, end)
        
        return moves

def solution(n):
    return hanoi(n, 1, 3)

print(solution(2))