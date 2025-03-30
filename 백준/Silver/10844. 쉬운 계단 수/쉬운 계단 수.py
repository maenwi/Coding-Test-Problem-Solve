MOD = 1_000_000_000

N = int(input())

# dp[n][k] = 길이가 n이고, 끝자리가 k인 계단 수의 개수
dp = [[0] * 10 for _ in range(N + 1)]

# 초기값: 길이 1일 때는 1~9까지만 1개씩 가능
for i in range(1, 10):
    dp[1][i] = 1

for n in range(2, N + 1):
    for k in range(10):
        if k > 0:
            dp[n][k] += dp[n - 1][k - 1]
        if k < 9:
            dp[n][k] += dp[n - 1][k + 1]
        dp[n][k] %= MOD

# 길이 N인 계단 수의 총합 (끝자리가 0~9인 모든 경우 합)
print(sum(dp[N]) % MOD)
