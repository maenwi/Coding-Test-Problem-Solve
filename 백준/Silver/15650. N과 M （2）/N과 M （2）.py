from itertools import combinations

N, M = map(int, input().split())

answer = list(combinations(map(str, range(1, N + 1)), M))

for a in answer:
    print(" ".join(a))