# 2022 KAKAO BLIND RECRUITMENT
# 신고 결과 받기
# https://school.programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    
    temp = []
    # New list to Store "a b" to ['a', 'b']
    for pair in report:
        a, b = pair.split()
        temp.append([a, b])
    
    # Keep only unique sublists in the new list
    seen = set()
    reportLst = []
    for sublist in temp:
        key = tuple(sublist)
        if key not in seen:
            reportLst.append(sublist)
            seen.add(key)
    
    # Keep Track of num Users banned reported by id_list user
    countTracker = {key: 0 for key in id_list}
    reporter = {}
    countReported = {}
    
    for sublist in reportLst:
        if sublist[0] not in reporter:
            reporter[sublist[0]] = []
        
        if sublist[0] in reporter:
            reporter[sublist[0]].append(sublist[1])
            
        if sublist[1] not in countReported:
            countReported[sublist[1]] = 0
            
        if sublist[1] in countReported:
            countReported[sublist[1]] += 1

    # Compare countReported with k
    banned = []
    for key, value in countReported.items():
        if value >= k:
            banned.append(key)
    
    for key, value in reporter.items():
        common_elements = len(set(reporter[key]).intersection(banned))
        countTracker[key] += common_elements   
    
    return list(countTracker.values())
    
#Test Cases
idLst1 = ["muzi", "frodo", "apeach", "neo"]
report1 = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k1 = 2
print(solution(idLst1, report1, k1), '\n')

idLst2 = ["con", "ryan"]
report2 = ["ryan con", "ryan con", "ryan con", "ryan con"]
k2 = 3
print(solution(idLst2, report2, k2))

# reporter = {}
# countReported = {}
# reportLst = [['a', 'b'], ['a', 'c'], ['b', 'c'], ['c', 'd']]
# countTracker = { 'a': 0, 'b': 0, 'c': 0 }

# for sublist in reportLst:
#     if sublist[0] not in reporter:
#         reporter[sublist[0]] = []
    
#     if sublist[0] in reporter:
#         reporter[sublist[0]].append(sublist[1])
        
#     if sublist[1] not in countReported:
#         countReported[sublist[1]] = 0
            
#     if sublist[1] in countReported:
#         countReported[sublist[1]] += 1
        
# banned = []
# for key, value in countReported.items():
#     if value >= 1:
#         banned.append(key)

# for key, value in reporter.items():
#     common_elements = len(set(reporter[key]).intersection(banned))
#     countTracker[key] += common_elements

# print("Reported Dict: ", reporter)
# print("countReported Dict: ", countReported)
# print("Banned: ", banned)
# print("Count Tracker: ", list(countTracker.values()))