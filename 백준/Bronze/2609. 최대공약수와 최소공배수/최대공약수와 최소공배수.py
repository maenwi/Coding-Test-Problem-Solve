a, b = map(int, input().split())

def find_gcd(a, b):
    if b > a:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a

def find_lcm(a, b, gcd = None):
    if b > a:
        a, b = b, a
    
    if gcd is None:
        gcd = find_gcd(a, b)

    return int(a * b / gcd)

gcd = find_gcd(a, b)
print(gcd)
print(find_lcm(a, b, gcd))