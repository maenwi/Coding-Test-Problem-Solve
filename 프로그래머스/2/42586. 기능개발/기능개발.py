from collections import deque

def solution(progresses, speeds):
    answer = []

    progresses_q = deque(progresses)
    speeds_q = deque(speeds)

    while progresses_q: # 모든 작업이 완료될 때 까지
        # 작업 진행
        progresses_q = deque(map(lambda x, y: x + y, progresses_q, speeds_q))
        count = 0

        while progresses_q and progresses_q[0] >= 100:
            count += 1
            progresses_q.popleft()
            speeds_q.popleft()

        if count > 0:
            answer.append(count)
    
    return answer