import numpy as np

# def solution(arr, k):

#     flatten_arr = np.ravel(arr)
#     sorted_arr = sorted(flatten_arr)
#     answer = sorted_arr[k-1]
            
#     return answer

def solution(arr, k):
    flatten_arr = []
    for sublist in arr:
        if isinstance(sublist, list):
            for element in sublist:
                flatten_arr.append(element)
        else:
            flatten_arr.append(sublist)
    sorted_arr = sorted(flatten_arr)
    answer = sorted_arr[k-1]
    return answer

print(solution([[5, 12, 4, 31], [24, 13, 11, 2], [43, 44, 19, 26], [33, 65, 20, 21]], 4))

# --------------------------------------------------------
# 세 개의 구분자
import re
def solution1(myStr):
    answer = []
    splitwords = '[abc]'
    answer = re.split(splitwords, myStr)
    answer = list(filter(None, answer))
    
    if len(answer) == 0:
        return ['EMPTY']
    
    return answer

print(solution1("baconlettucetomato"))
print(solution1("cabab"))

# --------------------------------------------------------
# 예산 소팅 문제
# def solution2(d, budget):
#     d.sort()
#     while budget < sum(d):
#         d.pop()
#     return len(d)

# Summer/Winter Coding(~2018)
# 예산
def solution2(d, budget):
    answer = 0
    sorted_d = sorted(d)

    for i in sorted_d:
        budget = budget - i
        if budget < 0:
            break
        answer += 1
    return answer

print(solution2([1, 3, 2, 5, 4], 9))
print(solution2([2, 2, 3, 3], 10))

# --------------------------------------------------------
# 햄버거 만들기 -- stack
def solution3(ingredient):
    answer = 0
    stack = []
    
    for i in ingredient:
        stack.append(i)
        if stack[-4:] == [1, 2, 3, 1]:
            answer += 1
            for j in range(4):
                stack.pop()
    return answer

print(solution3([2, 1, 1, 2, 3, 1, 2, 3, 1]))
print(solution3([1, 3, 2, 1, 2, 1, 3, 1, 2]))
print('\n')

# --------------------------------------------------------
# Summer/Winter Coding(~2018)
# 소수 만들기
def is_prime(n):
    if n < 2:
        return False
    # only need to check up to sqrt(n)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_prime_combinations(numbers):
    count = 0
    n = len(numbers)
    
    # The outer loop iterates from the first number to the third-to-last number, 
    # The middle loop iterates from the second number to the second-to-last number, 
    # The inner loop iterates from the third number to the last number.
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                combination_sum = numbers[i] + numbers[j] + numbers[k]
                if is_prime(combination_sum):
                    print(combination_sum)
                    count += 1
    return count

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7]
result = count_prime_combinations(numbers)
print("Total prime combinations:", result)

# --------------------------------------------------------
# 월간 코드 챌린지 시즌1
# 내적
# def solution(a, b):
#     return sum([x * y for x, y in zip(a,b)])

def inner_product(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]
    return answer

print(inner_product([1,2,3,4], [-3,-1,0,2]))
print(inner_product([-1,0,1], [1,0,-1]))

# --------------------------------------------------------
# 월간 코드 챌린지 시즌1
# 두 개 뽑아서 더하기

def allCombSumofTwoNumbers(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            num_sum = numbers[i] + numbers[j]
            answer.append(num_sum)
    answer = sorted(dict.fromkeys(answer)) # return sorted(list(set(answer)))
    return answer

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
