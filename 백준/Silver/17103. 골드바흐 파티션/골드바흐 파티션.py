def make_sieve(limit):
    primes = [True] * (limit + 1)
    primes[0] = False
    primes[1] = False

    for i in range(2, int(limit ** 0.5) + 1):
        if primes[i]: # i가 소수라면,
            # 그 소수의 배수들은 전부 제거
            for ii in range(i * i, limit + 1, i):
                primes[ii] = False
    
    return primes

import sys

gold_bach = dict()

is_prime = make_sieve(10000)
for even_number in range(4, 10001, 2):

    for i in range(even_number // 2, 1, -1):
        if is_prime[i] and is_prime[even_number - i]:
            gold_bach[even_number] = (i, even_number - i)
            break

input = sys.stdin.readline
T = int(input())
Ns = [int(input()) for _ in range(T)]

max_n = max(Ns)
is_prime = make_sieve(max_n)

results = []
for n in Ns:
    count = 0
    for i in range(2, n // 2 + 1):
        if is_prime[i] and is_prime[n - i]:
            count += 1
    results.append(str(count))

print("\n".join(results))