# 더 맵게
# https://school.programmers.co.kr/learn/courses/30/lessons/42626

# Using heapq data structure
from heapq import *

def solution(scoville, K):
    turns = 0
    heapify(scoville)
    
    while scoville[0] < K and len(scoville) > 1:
        # Remove first 2 elements
        e1 = heappop(scoville)
        e2 = heappop(scoville)
        # Add mixed data
        heappush(scoville, e1 + e2 * 2)
        turns += 1
        
    if scoville[0] >= K:
        return turns
    else:
        return -1

# Test Case
s1 = [1, 2, 3, 9, 10, 12]
k1 = 7
print(solution(s1, k1))


# heapq data structure automatically sorts data
# heappop() remove elements
# heappush() add elements

### Attempt 1
# Time Limit Exceeded
# from collections import deque

# def solution(scoville, K):
#     s = deque(sorted(scoville))
#     turns = 0
    
#     while s:
#         if s[0] < K:
#             s.append(s[0] + s[1]*2)
#             s.popleft()
#             s.popleft()
#             s = deque(sorted(list(s)))
#             turns += 1
            
#         if s[0] > K:
#             return turns
        
#         if len(s) == 1 and s[0] < K:
#             return -1
