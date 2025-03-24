from itertools import permutations

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort() # O(N log N)

combs = list(set(permutations(numbers, M)))

combs.sort() # O(N! log N!)

for comb in combs:
    print(" ".join([str(n) for n in comb]))
