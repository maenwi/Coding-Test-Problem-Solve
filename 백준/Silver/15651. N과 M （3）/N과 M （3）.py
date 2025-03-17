from itertools import product

N, M = map(int, input().split())

answer = list(product(map(str, range(1, N + 1)), repeat = M))

for a in answer:
    print(" ".join(a))