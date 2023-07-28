# ----------------------------------------------------------------------------------
# 다리를 지나는 트럭
# https://school.programmers.co.kr/learn/courses/30/lessons/42583

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_length
    
    while len(truck_weights) != 0:
        bridge.pop(0) # remove first element
        time += 1 
        
        if sum(bridge) + truck_weights[0] <= weight:
            bridge.append(truck_weights[0])
            truck_weights.pop(0)
        else:
            bridge.append(0)
    
    time += bridge_length
    
    return time

# Test Cases
print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))

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

