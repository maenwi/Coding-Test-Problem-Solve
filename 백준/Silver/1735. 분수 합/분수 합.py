n1, d1 = map(int, input().split())
n2, d2 = map(int, input().split())

def find_gcd(a, b):
    if b > a:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a

def find_lcm(a, b):
    if b > a:
        a, b = b, a
    
    gcd = find_gcd(a, b)

    return int(a * b / gcd)

denominator_answer = find_lcm(d1, d2)
m1 = denominator_answer // d1
m2 = denominator_answer // d2

numerator_answer = n1 * m1 + n2 * m2

gcd_answer = find_gcd(denominator_answer, numerator_answer)

print(f"{int(numerator_answer / gcd_answer)} {int(denominator_answer / gcd_answer)}")

