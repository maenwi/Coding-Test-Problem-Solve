import sys

input = sys.stdin.readline

n, d = -1, -1

while True:
    n, d = map(int, input().split())
    if n == 0 and d == 0:
        break

    if n % d == 0: # n이 d로 나누어 떨어지면,
        print("multiple")

    elif d % n == 0: #d가 n으로 나누어 떨어지면,
        print("factor")

    else:
        print("neither")