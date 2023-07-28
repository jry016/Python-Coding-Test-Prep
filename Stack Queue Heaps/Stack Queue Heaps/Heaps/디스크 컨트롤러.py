# HEAPS
# 디스크 컨트롤러
# https://school.programmers.co.kr/learn/courses/30/lessons/42627

from heapq import *

def solution(jobs):

    total_duration = 0
    current_time = 0
    i = 0
    start_time = -1
    heap = []
    
    while i < len(jobs):
        #print(f"Iteration: {i}")
        for job in jobs:
            #print(f"start_time: {start_time}, job[0]: {job[0]}, current_time: {current_time}")
            if start_time < job[0] <= current_time:
                heappush(heap, [job[1], job[0]]) # 힙에 push를 할 때는 작업의 소요 시간 기준으로 min heap이 만들어야한다
        
        if len(heap) > 0:
            current = heappop(heap)         # 현재 처리할 작업
            start_time = current_time       # 시작 시간 업데이트
            current_time += current[0]      # 현재 시간 += 작업 시간
            
            total_duration += (current_time - current[1])
            #print(f"Updated -- start_time: {start_time}, current_time: {current_time}, total: {total_duration}")
            
            i += 1                          # Iterate # of jobs processed
            
        else:
            current_time += 1 # Heap Len = 0 -- no more tasks
                              # 현재 시점을 다음 시간으로 넘어가기 위해 current_time += 1
    
    average_duration = int(total_duration / len(jobs))
    return average_duration
    
    
# Test Cases
jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs)) 