string1 = input().strip()
string2 = input().strip()

len1, len2 = len(string1), len(string2)
dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        if string1[i - 1] == string2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len1][len2])

# lcs 역추적
lcs = ""
while len1 > 0 and len2 > 0:
    if string1[len1-1] == string2[len2-1]: # 둘이 같으면 대각선으로 온 것
        lcs += string1[len1-1]
        len1 -= 1
        len2 -= 1
    
    elif dp[len1 - 1][len2] >= dp[len1][len2 - 1]:
        # 둘이 다른 경우, dp 테이블을 관찰해서 위쪽이 더 크다면
        len1 -= 1 #위쪽으로 이동
    
    else:
        # 둘이 다르면서, 왼쪽이 더 크다면
        len2 -= 1 #왼쪽으로 이동

print(lcs[::-1])
