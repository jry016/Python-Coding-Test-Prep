import math

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
# progresses = [93, 30, 55]
# speeds = [1, 30, 5]
days = [math.ceil((100 - progresses[i])/speeds[i]) for i in range(len(progresses))]
    
        
print("Days Left: ", days)

release = []
count = 1

for i in range(len(days)):
    found_bigger = True
    
    if i == (len(days) - 1):
        release.append(count)
        break
    
    for j in range(i + 1, len(days)):
            if days[j] > days[i]:
                found_bigger = True
                i = i + j - 1
                break
            else:
                count += 1

    if found_bigger:
        release.append(count)
        count = 1

    
        
print(release)