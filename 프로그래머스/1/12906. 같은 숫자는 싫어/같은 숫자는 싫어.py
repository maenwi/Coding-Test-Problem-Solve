from collections import deque

def solution(arr):
    answer = []

    q = deque(arr)
    prev = -1
    while q:
        current = q.popleft()
        if prev != current: # 새로운 숫자가 나왔으면 결과에 추가
            answer.append(current)
        prev = current
    
    return answer