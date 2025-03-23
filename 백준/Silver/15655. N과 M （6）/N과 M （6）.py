from itertools import combinations

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()

answer = list(combinations([str(n) for n in numbers], M))

for a in answer:
    print(" ".join(a))