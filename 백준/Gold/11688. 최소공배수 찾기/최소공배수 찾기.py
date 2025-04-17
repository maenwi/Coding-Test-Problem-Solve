# 소인수 분해 두 번이 필요함
# 두 수 중 하나를 갖고와서 체를 만들자.

def sieve(limit):
    primes = [True] * (limit + 1)
    
    primes[0] = False
    primes[1] = False

    for i in range(2, int(limit ** 0.5) + 1):
        if primes[i]:
            for ii in range(i * i, int(limit) + 1, i):
                primes[ii] = False
    
    return [i for i, num in enumerate(primes) if num]

from collections import defaultdict

def prime_factorization(n, primes):
    factors = defaultdict(int)
    for prime in primes:
        if prime * prime > n:
            break

        while n % prime == 0:
            factors[prime] += 1
            n //= prime
    
    if n > 1:
        factors[n] += 1
    
    return dict(factors)

def main():
    a, b, L = map(int, input().split())

    import math
    lcm = math.lcm(a, b)

    if L % lcm != 0:
        print("-1")
        return 

    primes = sieve(math.isqrt(L))

    L_factors = prime_factorization(L, primes)
    lcm_factors = prime_factorization(lcm, primes)

    answer = 1
    for k, power_L in L_factors.items():
        power_lcm = lcm_factors.get(k, 0)

        if power_lcm == power_L:
            continue

        answer *= (k ** power_L)

    print(answer)
    return

if __name__ == "__main__":
    main()
