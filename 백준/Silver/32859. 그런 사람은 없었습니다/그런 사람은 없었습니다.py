
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
S = int(input())

# -1 : 폼 제출 완료
# 0, 1, ... : 폼 제출이 딜레이된 시간
status = [0] * (N + 1)
delayed = set()
answer = []

for _ in range(M):
    i, t = map(int, input().split())

    # 폼 제출 완료
    if t == 0:
        status[i] = -1
        delayed.discard(i)
    
    # 돈 먼저 냄
    elif t == 1 and status[i] == 0:
        delayed.add(i)

    for p in delayed:
        if p == i or t == 1:
            continue
        status[p] += 1

        if status[p] == S:
            answer.append(p)

if answer:
    answer.sort()
    for a in answer:
        print(a)
else:
    print(-1)