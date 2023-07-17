# 2022 KAKAO TECH INTERNSHIP
# 두 큐 합 길게 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/118667

from collections import deque

def solution(queue1, queue2):
    result = 0
    queue1, queue2 = deque(queue1), deque(queue2)
    
    # keep track of the current sum for both queues 
    # update after each iteration --> avoid unnecessary sum calculations
    q1_sum, q2_sum = sum(queue1), sum(queue2)
    
    if (q1_sum + q2_sum) % 2 != 0:
            return -1
        
    while q1_sum != q2_sum:
        if queue1 == deque() or queue2 == deque():
            return -1
        
        if result == 4 * len(queue1):
            return -1
        
        if q2_sum > q1_sum:
            element = queue2.popleft()
            q1_sum += element
            q2_sum -= element
            queue1.append(element)
            result += 1
        
        elif q1_sum > q2_sum:
            element = queue1.popleft()
            q2_sum += element
            q1_sum -= element
            queue2.append(element)
            result += 1
        
        else:
            return result
    
    return result

# Test Cases
a = [3, 2, 7, 2]
aa = [4, 6, 5, 1]

b = [1, 2, 1, 2]
bb = [1, 10, 1, 2]

c = [1, 1]
cc = [1, 5]

d = [1, 2]
dd = [2, 4]

print(solution(a, aa))
print(solution(b, bb))
print(solution(c, cc))
print(solution(d, dd))


# V1 - Needs Shorter Runtime
# def solution(queue1, queue2):
#     result = 0
#     queue1 = deque(queue1)
#     queue2 = deque(queue2)
    
#     while sum(queue1) != sum(queue2):
#         if queue1 == deque() or queue2 == deque():
#             return -1
        
#         if sum(queue1) > sum(queue2):
#             queue2.append(queue1.popleft())
#             result += 1
        
#         if sum(queue2) > sum(queue1):
#             queue1.append(queue2.popleft())
#             result += 1
    
#     return result