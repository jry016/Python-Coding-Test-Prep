# 월간 코드 챌린지 시즌1
# 두 개 뽑아서 더하기.
# https://school.programmers.co.kr/learn/courses/30/lessons/68644

def allCombSumofTwoNumbers(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            num_sum = numbers[i] + numbers[j]
            answer.append(num_sum)
    answer = sorted(dict.fromkeys(answer)) # return sorted(list(set(answer)))
    return answer

# Test Cases
print(allCombSumofTwoNumbers([2,1,3,4,1]))
print(allCombSumofTwoNumbers([5,0,2,7]))
print(allCombSumofTwoNumbers([1, 2, 2, 3]))

# def solution(numbers):
#     numbers = sorted(numbers)
#     distinct = set(numbers) # distinct = dict.fromkeys(numbers)
    
#     answer = []
#     for i in range(len(distinct)):
#         for j in range(i + 1, len(numbers)):
#             num_sum = numbers[i] + numbers[j]
#             answer.append(num_sum)
#     answer = sorted(list(set(answer + numbers)))
#     return answer

# EDGE CASE: numbers = [1, 2, 2, 3],  expected output should be [3, 4, 5]
# However, the code above produces a different result due to the use of set() to remove duplicates. 
# When the set is created, it will eliminate the duplicate value of 2, 
# resulting in only two distinct values (1 and 3). 