# gcd(fib[n], fib[m]) % 1_000_000_007
# gcd(fib[n], fib[m]) == fib(gcd(n, m)) 성질
# 따라서, gcd(fib[n], fib[m]) % 1_000_000_007
#        == fib(gcd(n, m)) % 1_000_000_007

# 피보나치 수 계산해두기 vs 그때 그때 계산하기
# 계산해두는 경우에는 메모리 폭발할듯

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

T = int(input())
gcds = []
max_gcd = -1

for _ in range(T):
    n, m = map(int,input().split())
    print(get_fib(find_gcd(n, m)))
