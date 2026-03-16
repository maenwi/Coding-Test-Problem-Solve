import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

g = 0
for i in range(N):
    A[i] -= B
    g += 1
    
    if A[i] >= 0:
        q, r = divmod(A[i], C)
        g += q

        if r != 0:
            g += 1

print(g)
