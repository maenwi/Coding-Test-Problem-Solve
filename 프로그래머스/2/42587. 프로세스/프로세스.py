from collections import deque
from collections import Counter

def solution(priorities, location):
    priorities_q = deque([(idx, prior) for idx, prior in enumerate(priorities)])
    # 원본 위치, 우선순위를 기록한 deque 만들기

    priority_values = Counter(priorities)
    # 우선순위 값들이 몇 개 있는지 확인
    priority_sorted = list(priority_values.keys())
    priority_sorted.sort()
    max_priority = priority_sorted[-1]
    # 가장 큰 우선순위 확인

    count = 0
    # 몇 개의 항목들이 실행 됐는지 확인

    while priorities_q:
        idx, prior = priorities_q.popleft()
        # 맨 앞에 있는 task 확인
        if prior == max_priority: # 그 task가 가장 우선순위 task면?
            # 실행
            priority_values[prior] -= 1
            count += 1

            if idx == location: # 원하는 항목이 실행됐으면
                return count # 몇 번째로 실행됐는지 리턴

            if priority_values[prior] == 0:
                # 가장 큰 우선순위 항목들을 다 실행했음
                priority_sorted.pop() # 가장 큰 우선순위 값 빼고
                max_priority = priority_sorted[-1] # 업데이트
        
        else:
            priorities_q.append((idx, prior))