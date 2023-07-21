# Summer/Winter Coding(~2018)
# 소수 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12977

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
