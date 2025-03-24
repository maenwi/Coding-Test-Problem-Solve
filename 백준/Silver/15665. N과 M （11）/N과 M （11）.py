from itertools import product

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()

combs = list(set(product(numbers, repeat = M)))

combs.sort()

for comb in combs:
    print(" ".join([str(n) for n in comb]))
