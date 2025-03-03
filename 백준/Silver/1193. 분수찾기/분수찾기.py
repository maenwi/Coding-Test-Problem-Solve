n = int(input())

d = 1

while n > d:
    n -= d
    d += 1

# d+1이 분모 분자의 합
# 분자는 1부터 시작
n -= 1
nume = 1
deno = d

while n > 0:
    nume += 1
    deno -= 1
    n -= 1
printstring = f"{nume}/{deno}" if d % 2 == 0 else f"{deno}/{nume}"
print(printstring)