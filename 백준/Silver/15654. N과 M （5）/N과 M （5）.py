from itertools import permutations

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()

answer = list(permutations([str(n) for n in numbers], M))

for a in answer:
    print(" ".join(a))