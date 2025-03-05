def cal_comb(n, k):
    numer = 1
    denom = 1
    for num in range(1, k + 1):
        numer *= (n - (num - 1))
        denom *= num

    return int(numer/denom)

N, K = map(int, input().split())

if K > N - K:
    print(cal_comb(N, N-K))
else:
    print(cal_comb(N, K))