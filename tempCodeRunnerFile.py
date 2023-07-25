import math

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
days = []
for i in range(len(progresses)):
        time_b4_complete = math.ceil((100 - progresses[i])/speeds[i])
        days.append(time_b4_complete)
        
print("Days Left: ", days)

release = []
count = 0
for i in range(len(days)):
    if days[i] > days[i+1]:
        count += 1
        continue
    else:
        count = 0
        release.append(count)
        
print(release)