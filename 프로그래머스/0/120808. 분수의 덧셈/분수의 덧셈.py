def is_prime(n):
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0: # 나누어 떨어지면
            return False
    return True

def solution(numer1, denom1, numer2, denom2):
    denom = denom1 * denom2
    numer = numer1 * denom2 + numer2 * denom1

    PRIMES = [i for i in range(2, int((max(denom, numer) ** (1/2))) + 1) if is_prime(i)]

    for p in PRIMES:
        while denom % p == 0 and numer % p == 0:
            # 둘 다 나누어 떨어진다면 나눠줘야함
            denom /= p
            numer /= p

    return [int(numer), int(denom)]