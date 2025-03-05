from collections import deque

M, N, H = map(int, input().split())

box = []
# box[층][row][column]

ripen_tomato = []
not_ripen_tomato = set()

for h in range(H):
    a_floor = []
    for n in range(N):
        a_row = list(map(int, input().split()))

        # 토마토의 익은 정보를 입력
        for m in range(M):
            if a_row[m] == 1: # 익은 토마토 입력
                ripen_tomato.append((h, n, m))
            elif a_row[m] == 0: # 익지 않은 토마토
                not_ripen_tomato.add((h, n, m))

        a_floor.append(a_row)
    
    box.append(a_floor)

def solution(box, ripen_tomato, not_ripen_tomato):
    # 익지 않은 토마토가 없다면 return 0
    if len(not_ripen_tomato) == 0:
        return 0
    
    # 위, 아래, 앞쪽, 뒤쪽, 오른쪽, 왼쪽
    adjacents = [(+1, 0, 0), (-1, 0, 0), 
                 (0, +1, 0), (0, -1, 0),
                 (0, 0, +1), (0, 0, -1)]
    
    # bfs 준비
    current_ripen_tomato = deque(ripen_tomato)

    time = 0

    while True:
        
        # 시간 1 더해주고
        time += 1

        temp = deque() # 새로 익은 토마토들을 넣을 temp
        # 현재 익어있는 토마토들이 옆으로 익힘을 전파하는게 1타임임
        while current_ripen_tomato:
            cur_h, cur_r, cur_c = current_ripen_tomato.popleft()
            for dh, dr, dc in adjacents:
                new_h, new_r, new_c = cur_h + dh, cur_r + dr, cur_c + dc

                if 0 <= new_h < H and 0 <= new_r < N and 0 <= new_c < M:
                    # 맵을 멋어나지 않았고,
                    if box[new_h][new_r][new_c] == 0:
                        # 아직 안 익은 토마토가 있다면
                        box[new_h][new_r][new_c] = 1
                        # 해당 토마토 익음

                        temp.append((new_h, new_r, new_c))
                        
                        # 토마토가 익었기 때문에 아직 안 익은 토마토 제거
                        not_ripen_tomato.discard((new_h, new_r, new_c))
        
        current_ripen_tomato = temp
        
        # 내부 while문이 끝나면 한 타임이 끝
        if len(not_ripen_tomato) == 0:
            # 모든 토마토가 다 익었다면, 함수가 끝
            return time

        
        # 익은 토마토가 없는데, 아직 안 익은 토마토가 남아있다는 건?
        # 익을 수 없다는 것임.
        if len(current_ripen_tomato) == 0 and len(not_ripen_tomato) != 0:
            return -1
        
print(solution(box, ripen_tomato, not_ripen_tomato))