def find_gcd(a, b):
    if b > a:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a

a, b = map(int, input().split())
gcd = find_gcd(a, b)

print(int((a // gcd) * (b // gcd) * gcd))