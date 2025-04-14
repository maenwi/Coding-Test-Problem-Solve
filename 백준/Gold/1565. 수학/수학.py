import sys

input = sys.stdin.readline

len_d, len_m = map(int, input().split())
d = list(map(int, input().split()))
m = list(map(int, input().split()))

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

def find_gcd_divide_conquer(arr, left, right):
    if left == right:
        return arr[left]
    mid = (left + right) // 2
    left_gcd = find_gcd_divide_conquer(arr, left, mid)
    right_gcd = find_gcd_divide_conquer(arr, mid + 1, right)
    return find_gcd(left_gcd, right_gcd)

def find_lcm_divide_conquer(arr, left, right):
    if left == right:
        return arr[left]
    if right - left == 1:
        return find_lcm(arr[left], arr[right])
    
    mid = (left + right) // 2
    left_lcm = find_lcm_divide_conquer(arr, left, mid)
    right_lcm = find_lcm_divide_conquer(arr, mid + 1, right)
    return find_lcm(left_lcm, right_lcm)

def find_divisors(n):
    divisor_from_small = []
    divisor_from_big = []
    for d in range(1, int(n ** 0.5) + 1):
        if n % d == 0:
            big_divisor = n // d
            if big_divisor == d:
                divisor_from_small.append(d)
            else:
                divisor_from_small.append(d)
                divisor_from_big.append(big_divisor)
    
    return divisor_from_small + [d for d in divisor_from_big[::-1]]

lcm_d = find_lcm_divide_conquer(d, 0, len(d) - 1)
gcd_m = find_gcd_divide_conquer(m, 0, len(m) - 1)

divisors_gcd_m = find_divisors(gcd_m)

answer = 0
for divisor in divisors_gcd_m:
    if divisor % lcm_d == 0:
        answer += 1

print(answer)
