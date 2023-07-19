# KATTIS
# Pivot
# https://open.kattis.com/problems/pivot

n = int(input())
A = input()
A = [int(num) for num in A.split()]

# def pivot(n, A):
#     cnt = 0

#     for i in range(n):
#         isPivot = True
#         # Check values to the left
#         for j in range(0, i):
#             if A[j] >= A[i]:
#                 isPivot = False
#                 break
            
#         if isPivot:
#             # Check values to the right
#             for k in range(i+1, n):
#                 if A[i] <= A[k]:
#                     isPivot = False
#                     break
        
#         if isPivot:
#             cnt += 1
            
#     print(cnt)
    

def pivot(n, A):
    cnt = 0

    for i in range(n):
        # Check values to the left
        is_potential_pivot = True
        for j in range(0, i):
            if A[j] >= A[i]:
                is_potential_pivot = False
                break

        # Check values to the right
        if is_potential_pivot:
            for k in range(i+1, n):
                if A[i] <= A[k]:
                    is_potential_pivot = False
                    break

        if is_potential_pivot:
            cnt += 1

    print(cnt)
 
pivot(n, A)

# Test Cases
# 8
# 2 1 3 4 7 5 6 8
# Expected Output:3 

# 7
# 1 2 3 4 5 7 6
# Expected Output: 5

