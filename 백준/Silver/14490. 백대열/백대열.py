n, m = map(int, input().split(":"))

def find_gcd(a, b):
    if b > a:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a

gcd = find_gcd(n, m)
print(f"{n//gcd}:{m//gcd}")