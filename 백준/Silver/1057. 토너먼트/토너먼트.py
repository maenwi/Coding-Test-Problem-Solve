import sys
import math

input = sys.stdin.readline

N, Kim, Lim = map(int, input().split())

games = 1
while True:
    if abs(Kim - Lim) == 1 and max(Kim, Lim) % 2 == 0:
        break

    games += 1
    Kim = math.ceil(Kim / 2)
    Lim = math.ceil(Lim / 2)

print(f"{games}")
