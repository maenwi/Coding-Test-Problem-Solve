N, L = map(int, input().split())

dp = [(0, 0) for _ in range(101)]
dp[1] = (1, 0)
dp[2] = (2, 1)

for idx in range(3, 101):
    dp[idx] = (dp[idx - 1][0] + 1, dp[idx - 1][1] + (idx - 1))

def get_seq(N, L):
    for l in range(L, 101):
        if (N - dp[l][1]) % dp[l][0] == 0:
            start = int((N - dp[l][1]) // dp[l][0])

            if start >= 0: # 가능한 경우에만
                printstring = ""
                for d in range(l):
                    printstring = f"{printstring}{start + d} "
                print(printstring[:-1])
                return
            
    # 여기까지 왔다는건, 가능한 l을 못 찾은 것
    print(-1)
    return


get_seq(N, L)