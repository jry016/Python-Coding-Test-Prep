# 같은 숫자는 싫어
# https://school.programmers.co.kr/learn/courses/30/lessons/12906

# def uniqueArr(arr):
#     unique_elements = []
    
#     for i in range(len(arr)):
#         if i == (len(arr)-1) or arr[i] != arr[i+1]:
#             unique_elements.append(arr[i])
#     return unique_elements
 
# Test Cases
# print(uniqueArr([1,1,3,3,0,1,1]))    
# print(uniqueArr([4,4,4,3,3]))    

# i = 0
    # n = len(arr)
    # while i < n:
    #     if i == n-1 or arr[i] != arr[i+1]:
    #         unique_elements.append(arr[i])
    #     i += 1
        

# ----------------------------------------------------------------------------------
# 올바른 괄호
# https://school.programmers.co.kr/learn/courses/30/lessons/12909

# def brackets(s):
#     stack = []
    
#     for i in s:
#         if i == '(':
#             stack.append(i)
#         else:
#             if stack == []:
#                 return False
#             else:
#                 stack.pop()
    
#     if stack != []:
#         return False
                
#     return True

# Alternative Solution ----------------------------------------------------------
    # OPEN = '('
    # CLOSE = ')'
    # count = 0

    # for char in s:
    #     if char == OPEN:
    #         count += 1
    #     if char == CLOSE:
    #         count -= 1
    #     # count값이 0보다 작아졌다는 뜻은, 이미 짝이 맞지 않는다는 뜻이므로 early return
    #     # ex: '())', ')(' 이런 경우
    #     if count < 0:
    #         return False

# Test Cases
# print(brackets("()()"))
# print(brackets("(())()"))
# print(brackets(")()("))
# print(brackets("(()("))

# ----------------------------------------------------------------------------------
# 다리를 지나는 트럭
# https://school.programmers.co.kr/learn/courses/30/lessons/42583

# def solution(bridge_length, weight, truck_weights):
#     time = 0
#     bridge = [0] * bridge_length
    
#     while len(truck_weights) != 0:
#         bridge.pop(0) # remove first element
#         time += 1 
        
#         if sum(bridge) + truck_weights[0] <= weight:
#             bridge.append(truck_weights[0])
#             truck_weights.pop(0)
#         else:
#             bridge.append(0)
    
#     time += bridge_length
    
#     return time

# Alternative Solution -- Using Deque
# deque의 popleft() --> O(1)
# list의 pop(0) --> O(n)

# from collections import deque

# def solution(bridge_length, weight, truck_weights):
#     time = 0
#     bridge = deque([0] * bridge_length)
#     bridge_weight = 0
    
#     while truck_weights:
#         time += 1
#         bridge_weight -= bridge.popleft()
        
#         if bridge_weight + truck_weights[0] <= weight:
#             truck = truck_weights.pop(0)
#             bridge_weight += truck
#             bridge.append(truck)
#         else:
#             bridge.append(0)
    
#     time += bridge_length
    
#     return time

# print(solution(2, 10, [7, 4, 5, 6]))
# print(solution(100, 100, [10]))
# print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))

# ----------------------------------------------------------------------------------
# 주식 가격 거래
# https://school.programmers.co.kr/learn/courses/30/lessons/42584

#def Stocks(prices):
