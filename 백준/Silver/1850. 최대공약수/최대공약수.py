a, b = map(int, input().split())

def find_gcd(a, b):
    if b > a:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a

print("1" * find_gcd(a, b))