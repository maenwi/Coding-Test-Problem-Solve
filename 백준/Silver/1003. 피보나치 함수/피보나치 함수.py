T = int(input())

answer = []

dp = [(0, 0) for _ in range(41)]
dp[0], dp[1] = (1, 0),  (0, 1)

for idx in range(2, 41):
    dp[idx] = (dp[idx-2][0] + dp[idx-1][0], dp[idx-2][1] + dp[idx-1][1])

for t in range(T):
    N = int(input())
    answer.append(f"{dp[N][0]} {dp[N][1]}")

for a in answer:
    print(a)