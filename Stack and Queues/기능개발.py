# 기능 개발
# https://school.programmers.co.kr/learn/courses/30/lessons/42586

import math

def solution(progresses, speeds):
    release = []
    days = [math.ceil((100 - progresses[i])/speeds[i]) for i in range(len(progresses))]
    # progresses = [math.ceil((100 - a) / b) for a, b in zip(progresses, speeds)]
    
    curr_max_idx = 0
    
    for i in range(len(days)):
        if days[i] > days[curr_max_idx]:
            # i - curr_max_idx = # of items smaller than value at curr_max_idx
            release.append(i - curr_max_idx)
            curr_max_idx = i # update current max
    release.append(len(progresses) - curr_max_idx)
    
    return release

# Test Cases
p1 = [93, 30, 55]
s1 = [1, 30, 5]

p2 = [95, 90, 99, 99, 80, 99]
s2 = [1, 1, 1, 1, 1, 1]

print(solution(p1, s1))
print(solution(p2, s2))