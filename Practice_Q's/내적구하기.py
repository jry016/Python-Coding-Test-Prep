# 월간 코드 챌린지 시즌1
# 내적
# https://school.programmers.co.kr/learn/courses/30/lessons/70128


# def solution(a, b):
#     return sum([x * y for x, y in zip(a,b)])

def inner_product(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]
    return answer

# Test Cases
print(inner_product([1,2,3,4], [-3,-1,0,2]))
print(inner_product([-1,0,1], [1,0,-1]))
