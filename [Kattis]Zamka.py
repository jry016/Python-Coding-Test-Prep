# KATTIS
# Zamka
# https://open.kattis.com/problems/zamka

L = int(input())
D = int(input())
X = int(input())

# Sum of digits
def digitSum(num):
    return sum(map(int, str(num)))

def Zamka(L, D, X):
    currMax = 0
    currMin = 10001
    
    for i in range(L, D+1):
        if (digitSum(i) == X and i > currMax):
            currMax = i
        if (digitSum(i) == X and i < currMin):
            currMin = i

    print(currMin)
    print(currMax)

Zamka(L, D, X)

# def digitSum(num):
#     digits = [int(d) for d in str(num)]
#     return sum(digits)

# def digitSum(num):
#     total = 0
#     while num > 0:
#         digit = num % 10
#         total += digit
#         num //= 10
#     return total


# Test Cases
# i1 = [1, 100, 4] # 4 40 
# i2 = [100, 500, 12] # 129 480
# i3 = [1, 10000, 1] # 1 10000

