# 연습문제
# 햄버거 만들기 -- stack
# https://school.programmers.co.kr/learn/courses/30/lessons/133502

def solution3(ingredient):
    answer = 0
    stack = []
    
    for i in ingredient:
        stack.append(i)
        if stack[-4:] == [1, 2, 3, 1]:
            answer += 1
            for j in range(4):
                stack.pop()
    return answer

# Test Cases
print(solution3([2, 1, 1, 2, 3, 1, 2, 3, 1]))
print(solution3([1, 3, 2, 1, 2, 1, 3, 1, 2]))
