A, B = map(int, input().split())

def get_exp(num):
    result = 0
    while (1 << result) <= num:
        result += 1
    return result - 1

dp = [0] * 60 
dp[0] = 0  # 1~1까지의 1 개수는 0
for i in range(1, 60):
    dp[i] = dp[i-1] * 2 + (1 << (i-1))

def count_ones(n):
    if n <= 0:
        return 0
    k = get_exp(n)
    msb_count = n - (1 << k) + 1
    return dp[k] + msb_count + count_ones(n - (1 << k))


print(count_ones(B) - count_ones(A-1))