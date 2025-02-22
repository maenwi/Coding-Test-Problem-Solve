from collections import deque

N, M = map(int, input().split())

maze = []
for _ in range(N):
    a_row = list(map(int, list(input())))
    maze.append(a_row)

visited = [[0 for _ in range(M)] for _ in range(N)]

# 처음 시작
queue = deque([(0, 0)])
visited[0][0] = 1

movement = [(+1,0),(-1,0),(0,+1),(0,-1)]
# 위 아래 오른 왼

while queue:
    cur_r, cur_c = queue.popleft()
    
    for dr, dc in movement:
        nr, nc = cur_r + dr, cur_c + dc

        # 맵 밖으로 나가려하거나, 이미 방문한 곳을 가려고 하거나, 벽을 뚫고 가려고 한다면
        if ((nr < 0 or nr > N - 1) or  
            (nc < 0 or nc > M - 1) or
            visited[nr][nc] >= 1 or
            maze[nr][nc] == 0):
            continue
        
        else:
            visited[nr][nc] = visited[cur_r][cur_c] + 1
            queue.append((nr, nc))
        
        if nr == N - 1 and nc == M - 1:
            print(visited[nr][nc])
            break