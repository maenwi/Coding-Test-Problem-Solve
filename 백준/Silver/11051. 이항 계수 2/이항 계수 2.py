# 10,007 : 소수임

MOD = 10007 # 소수 -> 페르마 소정리 활용

N, K = map(int, input().split())

FACTORIAL_MODS = [1] * (N + 1)
for idx in range(2, N + 1):
    FACTORIAL_MODS[idx] = (FACTORIAL_MODS[idx - 1] * idx) % MOD

# 페르마 소정리 활용
def modulo_inverse(base, mod):
    # pow의 시간 복잡도는 log b
    return pow(base, mod - 2, mod)

def solution(n, k, mod):
    # nC0, nCn 은 전부 1
    if k == 0 or k == n:
        return 1
    
    numerator = FACTORIAL_MODS[n]
    denominator = (FACTORIAL_MODS[k] * FACTORIAL_MODS[n - k]) % mod
    
    return (numerator * modulo_inverse(denominator, mod)) % mod

print(solution(N, K, MOD))
