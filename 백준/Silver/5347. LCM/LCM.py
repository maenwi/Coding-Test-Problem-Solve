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

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(find_lcm(a, b))