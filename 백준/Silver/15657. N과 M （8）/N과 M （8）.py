from itertools import combinations_with_replacement

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()

answer = list(combinations_with_replacement([str(n) for n in numbers], M))

for a in answer:
    print(" ".join(a))