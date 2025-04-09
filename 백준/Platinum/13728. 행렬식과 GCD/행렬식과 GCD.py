
def matrix_multi_2x2(a, b, mod):
    return [
        [(a[0][0]*b[0][0] + a[0][1]*b[1][0]) % mod, (a[0][0]*b[0][1] + a[0][1]*b[1][1]) % mod],
        [(a[1][0]*b[0][0] + a[1][1]*b[1][0]) % mod, (a[1][0]*b[0][1] + a[1][1]*b[1][1]) % mod]
    ]

def matrix_power(mat, power):
    result = [[1, 0], [0, 1]]  # 단위 행렬
    while power:
        if power % 2 == 1:
            result = matrix_multi_2x2(result, mat, 1_000_000_007)
        mat = matrix_multi_2x2(mat, mat, 1_000_000_007)
        power //= 2
    return result

def get_fib(n):
    if n == 0:
        return 0
    base = [[1, 1], [1, 0]]
    result = matrix_power(base, n-1)
    return result[0][0]  # F(n)

def find_gcd(a, b):
    if b > a:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a

N = int(input())

S = 0
for i in range(2, N + 2):
    S += get_fib(find_gcd(i, N + 1))

print(S % 1_000_000_007)