def check_primes(n):
    primes = [True] * (n + 1)

    primes[0] = False
    primes[1] = False

    for p in range(2, n + 1):
        if primes[p]:
            for not_prime in range(p * p, n + 1, p):
                primes[not_prime] = False
    
    return primes

M, N = map(int, input().split())

is_primes = check_primes(N)

for i, is_prime in enumerate(is_primes):
    if i >= M and is_prime:
        print(i)