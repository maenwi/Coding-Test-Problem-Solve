N = int(input())

prev = None
numbers = []
for _ in range(N):
    if prev is None:
        prev = int(input())
    else:
        cur = int(input())
        numbers.append(cur - prev)
        prev = cur

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

gcd = gcd_divide_conquer(numbers, 0, len(numbers) - 1)

answer = 0
for number in numbers:
    answer += (number // gcd - 1)

print(answer)