# IDEA
# 모든 수를 M으로 나눈 나머지가 같다
# == 임의의 두 수의 차는 M의 배수

def find_gcd(a, b):
    if b > a:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a

def gcd_divide_conquer(arr, left, right):
    if left == right:
        return arr[left]
    mid = (left + right) // 2
    left_gcd = gcd_divide_conquer(arr, left, mid)
    right_gcd = gcd_divide_conquer(arr, mid + 1, right)
    return find_gcd(left_gcd, right_gcd)

def find_divisor(n):
    divisor_from_small = []
    divisor_from_big = []
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            big_divisor = n // d
            if big_divisor == d:
                divisor_from_small.append(d)
            else:
                divisor_from_small.append(d)
                divisor_from_big.append(big_divisor)
    
    return divisor_from_small + [d for d in divisor_from_big[::-1]]

N = int(input())

numbers = []
for _ in range(N):
    numbers.append(int(input()))

differences = set()
for i in range(N - 1):
    for ii in range(i + 1, N):
        differences.add(abs(numbers[ii] - numbers[i]))

differences = list(differences)

gcd = gcd_divide_conquer(differences, 0, len(differences) - 1)

answer = find_divisor(gcd) + [gcd]
answer = [str(a) for a in answer]
print(" ".join(answer))