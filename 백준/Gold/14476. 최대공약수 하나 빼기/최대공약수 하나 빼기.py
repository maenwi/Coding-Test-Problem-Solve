def find_gcd(a, b):
    if b > a:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a

N = int(input())
numbers = list(map(int, input().split()))

# 그때그때 숫자를 빼서 gcd를 계산하는게 아니라,
# 특정 숫자를 기준으로, 그 숫자보다 앞선 값들의 gcd, 그 숫자 이후 값들의 gcd를 계산해두면
# 특정 숫자를 뺐을 때 좌우 gcd의 gcd로 빠르게 구할 수 있음.
# i번째 숫자를 뺐을 때, gcd(dp_left[i], dp_right[i]) 로 구하고 싶음
# dp_left[i] : 0번 숫자부터 i 번째 숫자까지의 gcd
# dp_right[i]: i번 숫자부터, N-1 까지의 gcd

dp_left = [0] * N
dp_left[0] = numbers[0]
for idx in range(1, N):
    dp_left[idx] = find_gcd(dp_left[idx - 1], numbers[idx])

dp_right = [0] * N
dp_right[N - 1] = numbers[N - 1]
for idx in range(N-2, -1, -1):
    dp_right[idx] = find_gcd(dp_right[idx + 1], numbers[idx])

max_gcd = -1
max_idx = None

for idx in range(N):
    if idx == 0:
        gcd = dp_right[idx + 1]
    elif idx == N - 1:
        gcd = dp_left[idx - 1]
    else:
        gcd = find_gcd(dp_left[idx - 1], dp_right[idx + 1])
    
    if gcd >= max_gcd:
        if numbers[idx] % gcd != 0:
            max_gcd = gcd
            max_idx = idx

if max_gcd != -1:
    print(f"{max_gcd} {numbers[max_idx]}")
else:
    print("-1")