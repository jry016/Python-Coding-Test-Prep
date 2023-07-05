# 2019 KAKAO BLIND RECRUITMENT CODING TEST
# 실패율

# def countDistinctElements(n, arr):
#     item_counter = {}
#     for element in arr:
#         if element in item_counter:
#             item_counter[element] += 1
#         else:
#             item_counter[element] = 1
    
#     distinct_counts = {item: count for item, count in item_counter.items()}
#     print(distinct_counts)
#     # sorted() is used to sort the items of the dictionary my_dict based on their values. 
#     # The key=lambda x: x[1] specifies that the sorting should be based on the second element 
#     # The reverse=True parameter is used to sort the dictionary in descending order.
#     distinct_counts = dict(sorted(distinct_counts.items(), key = lambda x: x[1], reverse = True))
#     return distinct_counts

# def failureRate(n, arr):
#     failure_rate = {key: value/len(arr) for key, value in arr.items()}
#     failure_list = failure_rate.keys()
#     return failure_list
        
# def solution(N, stages):
#     answer = failureRate(N, countDistinctElements(N, stages))
#     return answer

# stages = [2, 1, 2, 6, 2, 4, 3, 3]

# print(countDistinctElements(5, stages))
# print(solution(5, stages))

def solution(N, stages):
    total = len(stages)
    failures = {}
    
    for i in range(1, N + 1):
        count = stages.count(i) 
        if count == 0:
            fail = 0
        else:
            fail = count / total
        
        total = total - count
        failures[i] = fail # add stage# and # of failures to dictionary
    
    answer = sorted(failures, key = lambda x: failures[x], reverse = True)
    return answer

stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(5, stages))