from itertools import combinations_with_replacement

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()

combs = list(set(combinations_with_replacement(numbers, M)))

combs.sort()

for comb in combs:
    print(" ".join([str(n) for n in comb]))
