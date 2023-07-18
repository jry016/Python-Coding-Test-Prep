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