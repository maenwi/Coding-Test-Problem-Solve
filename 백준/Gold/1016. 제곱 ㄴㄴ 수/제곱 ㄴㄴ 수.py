# N이 주어지면, N 까지의 소수를 확인하는 함수
# 에라토스테네스의 체를 이용
def primes_upto_n(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0과 1은 소수가 아님

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    return primes
# O(sqrt(N))

# (소수)^2의 배수를 제외한 나머지 숫자들이 제곱 ㄴㄴ 수임

minimum, maximum = map(int, input().split())

primes = primes_upto_n(int(maximum ** 0.5) + 1)
# O(sqrt(maximum))

# minimum부터 maximum까지의 숫자에서 (소수)^2의 배수를 빼면 됨.
size = maximum - minimum + 1
is_square_free = [True] * size

count = size  # 제곱 ㄴㄴ 수 개수

primes = primes_upto_n(int(maximum ** 0.5) + 1)

for prime in primes:
    square = prime * prime
    # minimum 이후 처음으로 나타나는 square의 배수 확인
    start = ((minimum + square - 1) // square) * square
    for j in range(start, maximum + 1, square):
        # idx 맞춰주기
        idx = j - minimum
        if is_square_free[idx]:
            is_square_free[idx] = False
            count -= 1

print(count)