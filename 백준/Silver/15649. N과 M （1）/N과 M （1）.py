from itertools import permutations

N, M = map(int, input().split())

answer = list(permutations(map(str, range(1, N + 1)), M))

for a in answer:
    print(" ".join(a))