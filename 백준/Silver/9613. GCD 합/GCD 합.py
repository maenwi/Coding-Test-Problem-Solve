def find_gcd(a, b):
    if b > a:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a

from itertools import combinations
t = int(input())
answers = []

for _ in range(t):
    total_gcd = 0
    seq = list(map(int, input().split()))

    for a, b in list(combinations(seq[1:], 2)):
        total_gcd += find_gcd(a, b)

    answers.append(total_gcd)

for a in answers:
    print(a)