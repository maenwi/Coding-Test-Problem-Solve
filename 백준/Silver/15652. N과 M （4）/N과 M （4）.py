from itertools import combinations_with_replacement

N, M = map(int, input().split())

answer = list(combinations_with_replacement(map(str, range(1, N + 1)), M))

for a in answer:
    print(" ".join(a))