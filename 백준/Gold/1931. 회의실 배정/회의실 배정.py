N = int(input())

meetings = []

for _ in range(N):
    s, e = map(int, input().split())
    meetings.append((s, e))

meetings.sort(key = lambda x:(x[1], x[0]))

schedule = []

prev_end = -1
for meet in meetings:
    if prev_end <= meet[0]: # 이번 미팅이, 전 미팅 종료보다 이후에 시작한다면
        schedule.append(meet)
        prev_end = meet[1] # 이전 미팅의 종료 시간 입력

print(len(schedule))