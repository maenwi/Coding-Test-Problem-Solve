def find_gcd(a, b):
    if b > a:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a

T = int(input())
answers = []
for _ in range(T):
    a, b = map(int, input().split())
    gcd = find_gcd(a, b)

    answers.append(int((a // gcd) * (b // gcd) * gcd))

for answer in answers:
    print(answer)