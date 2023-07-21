# KATTIS
# Pivot
# https://open.kattis.com/problems/pivot
# Reference http://mycode.doesnot.run/2018/04/11/pivot/

# Version 4 from Reference
def main():
    n = int(input())
    A = [int(num) for num in input().split()]
    #A = list(map(int, input().split()))
    
    cnt = 0
    
    min_right = [float('inf') for _ in range(n)]
    for i in range(n-2, -1, -1):  
        min_right[i] = min(min_right[i+1], A[i+1])
    
    max_left = [0 for _ in range(n)]
    max_left[0] = A[0]
    for i in range(1, n):
        max_left[i] = max(max_left[i-1], A[i-1])
    
    for i in range(0, n):
        print(f"A[i]: {A[i]}, Max_left: {max_left[i]}, Min_right: {min_right[i]}")
        if A[i] >= max_left[i] and A[i] < min_right[i]:
            cnt += 1
            print(cnt)
            
    print(cnt)
    
if __name__ == '__main__':  
    main()

# Method 3
# Time Complexity: O(3n) -- doesnt work
# n = int(input())
# A = [int(num) for num in input().split()] # #A = list(map(int, input().split()))
# def pivot3(n, A):
#     cnt = 0
    
#     max_left = []
#     curr_max = A[0]
#     for i in range(0, n):
#         curr_max = max(curr_max, A[i])  
#         max_left.append(curr_max)

#     min_right = []
#     curr_min = float('inf') 
#     for i in range(n-1, -1, -1):  
#         curr_min = min(curr_min, A[i])  
#         min_right.insert(0, curr_min)
    
#     # print(max_left)
#     # print(min_right)
            
#     for i in range(0, n):
#         print(f"A[i]: {A[i]}, Max_left: {max_left[i]}, Min_right: {min_right[i]}")
#         if A[i] >= max_left[i] and A[i] <= min_right[i]:
#             cnt += 1
#             print(cnt)
#     print(cnt)
       
# n = 8
# A = [2, 1, 3, 4, 7, 5, 6, 8]
# pivot3(n, A)  # Output: 3

# n = 7
# A = [1, 2, 3, 4, 5, 7, 6]
# pivot3(n, A)  # Output: 5

# Method 2: To find pivots through array indexing
# Time Complexity: Still O(n^2) 
# Min, Max functions have O(n)
# def pivot2(n, A):
#     cnt = 0
#     max_left = A[0]
#     min_right = min(A[1:])
#     print(A)
#     for i in range(0, n):
#         if A[i] >= max_left and A[i] <= min_right:
#             cnt += 1
        
#         max_left = max(max_left, A[i])
#         if i < n - 1:
#             min_right = min(A[i + 1:])
#         else:
#             min_right = float('inf')
            
#         print(f"A[i]: {A[i]}, Max_left: {max_left}, Min_right: {min_right}")
#         print(cnt)
        
#     print(cnt)

### Naive Method 1 to Find Pivot
# Time Complexity O(n^2)
# def pivot(n, A):
#     cnt = 0
#     for i in range(0, n):
#         # Check values to the left
#         is_potential_pivot = True
          
#         for j in range(0, i): 
#             # if value of 
#             if A[j] > A[i]:
#                 is_potential_pivot = False
#                 break

#         # Check values to the right
#         if is_potential_pivot:
#             for k in range(i+1, n):
#                 if A[k] <= A[i] :
#                     is_potential_pivot = False
#                     break

#         if is_potential_pivot:
#             cnt += 1

#     print(cnt)
 
# pivot(n, A)


# Test Cases
# 8
# 2 1 3 4 7 5 6 8
# Expected Output:3 

# 7
# 1 2 3 4 5 7 6
# Expected Output: 5

