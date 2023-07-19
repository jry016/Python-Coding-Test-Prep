# KATTIS
# Greedily Increasing Subsequence
# https://open.kattis.com/problems/greedilyincreasing

N = int(input())
user_input = input()
A = [int(num) for num in user_input.split()]

def gis(N, A):
    gis = [A[0]]

    for i in range(1, N):
        element = A[i]
        if element > gis[-1]:
            gis.append(element)
    
    print(len(gis))
    # unpack gis elements with spaces
    print(*gis)
        
gis(N, A)

# Test Cases
# 7
# 2 3 1 5 4 7 6
# Expected Output: 
# 4
# 2 3 5 7
#
# 5
# 1 2 3 4 5
# Expected Output: 
# 5
# 1 2 3 4 5
#
# 5
# 5 4 3 2 1
# Expected Output: 
# 1
# 5
