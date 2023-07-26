# HEAPS
# 이중우선순위큐
# https://school.programmers.co.kr/learn/courses/30/lessons/42628

def solution(operations):
    answer = []
    return answer

# Test Case
# operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
# print(solution(operations)) #[0, 0]

# operations2 = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
# print(solution(operations2)) #[333, -45]

# ### Attempt 1: Runtime Error
# from heapq import *

# def solution(operations):
#     op = [[a,int(b)] for a, b in [pair.split() for pair in operations]]
    
#     heap = []
#     for i in op:
#         if i[0] == "I":
#             heappush(heap, i[1])
        
#         # Remove Max Value from Heap
#         elif i[0] == "D" and i[1] == 1:
#             if len(heap) != 0:
#                 max_val = max(heap)
#                 heap.remove(max_val)
                
#         # Remove Min Value from Heap
#         else:
#             heappop(heap)
        
#     if not heap:
#         return [0, 0]
#     else:
#         return [max(heap), min(heap)]
