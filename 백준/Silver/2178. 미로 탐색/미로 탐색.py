N, M = map(int, input().split())

maze = []
for _ in range(N):
    maze.append(list(map(int, list(input()))))

from collections import deque

q = deque([(0, 0)])

# 하 상 좌 우
moves = [(-1, 0), (+1, 0), (0, -1), (0, +1)]

while q:
    cur_r, cur_c = q.popleft()

    if cur_r == N - 1 and cur_c == M - 1:
        print(maze[cur_r][cur_c])

        break

    for dr, dc in moves:
        new_r, new_c = cur_r + dr, cur_c + dc

        if 0 <= new_r < N and 0 <= new_c < M and maze[new_r][new_c] == 1:
            # 맵을 벗어나지 않고, 벽으로 막혀있지 않으며, 해당 방향으로 갈 수 있다면면

            maze[new_r][new_c] = maze[cur_r][cur_c] + 1
            q.append((new_r, new_c))

