# IDEA
# 2981번과 유사

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

N, S = map(int, input().split())
As = list(map(int, input().split()))

differences = [abs(A - S) for A in As]

gcd = gcd_divide_conquer(differences, 0, len(differences) - 1)
print(gcd)