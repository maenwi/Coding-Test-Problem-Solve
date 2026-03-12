import sys

input = sys.stdin.readline

T = int(input())

Q, D, N, P = 25, 10, 5, 1

for _ in range(T):
    m = int(input())

    q, m = divmod(m, Q)
    d, m = divmod(m, D)
    n, m = divmod(m, N)
    p, m = divmod(m, P)

    print(f"{q} {d} {n} {p}")
    