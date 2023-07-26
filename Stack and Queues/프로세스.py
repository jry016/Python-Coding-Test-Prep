# 프로세스
# https://school.programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque

def solution(priorities, location):
    priorities = deque(priorities)
    count = 0

    # while priorities queue is not empty
    while priorities:
        max_priority = max(priorities) # find the maximum priority value

        if priorities[0] != max_priority:
            priorities.append(priorities.popleft())
            
            # Update location information
            if location == 0: 
                location = len(priorities) - 1 # since task has been moved to the back
            else:
                location -= 1 # deque gets rotated around by 1

        else:   # when priorities[0] == max
            if location == 0: 
                count += 1 
                break 
            
            else:
                priorities.popleft() # remove element 
                count += 1 
                location -= 1 

    return count

# Test Cases
p1 = [2, 1, 3, 2]
l1 = 2

p2 = [1, 1, 9, 1, 1, 1]
l2 = 0

print(solution(p1, l1))
print(solution(p2, l2))

### Attempt 1:
# def solution(priorities, location):
    
#     target = priorities[location] # target value of when target is processed
#     ordered_tasks = deque(sorted(list(priorities), reverse = True))
#     priorities = deque(priorities)
    
#     count = 1 # count which order target value is processed
#     while ordered_tasks:
#         for i in range(len(ordered_tasks)):
#             if ordered_tasks[i] != priorities[i]:
#                 priorities.append(priorities.popleft())
#                 priorities.popleft()
            
#             elif ordered_tasks[i] == priorities[i]:
#                 ordered_tasks.popleft()
#                 priorities.popleft()
#                 count += 1
                
#                 if ordered_tasks[i] == target:
#                     answer = count

#     return answer