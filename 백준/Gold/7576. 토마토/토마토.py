import sys

from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
box = [[0]*N for _ in range(M)]

# 리스트랑 덱은 비어있으면 False
unripe_tomatos = set()
ripe_tomatos = deque([])

for r in range(M):
    box[r] = list(map(int, input().split()))

    for c in range(N):
        if box[r][c] == 0:
            unripe_tomatos.add((r, c))

        elif box[r][c] == 1:
            ripe_tomatos.append((r, c))

def solution(box, ripe_tomatos, unripe_tomatos):
    adjacents = [(1,0),(-1,0),(0,1),(0,-1)]

    time = 0
    # 이 while문은 시간의 흐름 기록
    while True:
        # 종료 조건
        # 안 익은 토마토가 없거나
        if not unripe_tomatos:
            return time
        
        # 안 익은 토마토가 있는데, 더 익은 토마토가 없으면
        elif unripe_tomatos and not ripe_tomatos:
            return -1
        
        time += 1
        # print(f"Time : {time:2}")
        # 반복
        temp_ripe_tomatos = deque([])

        while ripe_tomatos:
            tomato_r, tomato_c = ripe_tomatos.popleft()

            for dr, dc in adjacents:
                nr, nc = tomato_r + dr, tomato_c + dc

                # 맵을 벗어나거나
                if nr < 0 or nr >= M or nc < 0 or nc >= N:
                    continue
                
                # 토마토가 이미 익었거나, 토마토가 없으면
                elif box[nr][nc] == 1 or box[nr][nc] == -1:
                    continue

                else:
                    # print(f"{nr:2}, {nc:2} ripe by {tomato_r:2}, {tomato_c:2}")
                    unripe_tomatos.remove((nr, nc))
                    temp_ripe_tomatos.append((nr, nc))
                    box[nr][nc] = 1

        ripe_tomatos = temp_ripe_tomatos
        
time = solution(box, ripe_tomatos, unripe_tomatos)
print(time)