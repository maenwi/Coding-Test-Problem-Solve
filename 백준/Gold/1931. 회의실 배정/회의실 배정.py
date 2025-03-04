N = int(input())

meetings = []
for _ in range(N):
    meetings.append(tuple(map(int, input().split())))

meetings.sort(key = lambda meet:(meet[1], meet[0]))

prev_end = -1
count = 0
for meet in meetings:
    if meet[0] >= prev_end:
        # 이번 회의가 이전 회의 종료 시간 이후에 시작한다면,
        count += 1 # 회의 개수 + 1
        prev_end = meet[1] # 이전 회의 종료시간 업데이트

print(count)