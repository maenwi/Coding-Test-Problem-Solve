from itertools import product

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()

answer = list(product([str(n) for n in numbers], repeat = M))

for a in answer:
    print(" ".join(a))