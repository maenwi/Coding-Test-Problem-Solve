MOD = 1000000007 # 소수 -> 페르마 소정리 활용

# 입력 빋기
M = int(input())

max_N = 0
Ns, Ks = [], []
for _ in range(M):
    N, K = map(int, input().split())
    Ns.append(N)
    Ks.append(K)

    # max_N 업데이트
    if max_N < N:
        max_N = N

# max_N에 대해 팩토리얼 계산 O(N)
FACTORIAL_MODS = [1] * (max_N + 1)
for idx in range(2, max_N + 1):
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

# O(M)
for idx in range(M):
    print(solution(Ns[idx], Ks[idx], MOD))

# 최종시간 복잡도 O(M + N)
