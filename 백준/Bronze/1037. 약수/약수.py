N = int(input())

divisors = list(map(int, input().split()))

min_divisor = 1000000
max_divisor = -1
for divisor in divisors:
    if divisor >= max_divisor:
        max_divisor = divisor
    if divisor <= min_divisor:
        min_divisor = divisor

print(min_divisor * max_divisor)