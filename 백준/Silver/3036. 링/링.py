def find_gcd(a, b):
    if b > a:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a

N = int(input())
rings = list(map(int, input().split()))

first = rings[0]

answers = []
for ring in rings[1:]:
    gcd = find_gcd(first, ring)
    answers.append(f"{first//gcd}/{ring//gcd}")

print("\n".join(answers))