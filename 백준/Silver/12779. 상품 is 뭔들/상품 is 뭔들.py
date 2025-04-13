import math

a, b = map(int, input().split())

total = b - a
count = math.isqrt(b) - math.isqrt(a)

if count == 0:
    print("0")
else:
    g = math.gcd(count, total)
    print(f"{count//g}/{total//g}")
