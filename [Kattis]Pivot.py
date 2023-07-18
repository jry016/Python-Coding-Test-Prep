# KATTIS
# Pivot
# https://open.kattis.com/problems/pivot

n = int(input())
A = input()
A = [int(num) for num in A.split()]

def pivot(n, A):
    cnt = 0
    pivot = A[n-1]
    for i in A:
        