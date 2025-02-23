from collections import deque

# 모든 노드를 순회하면서
# 1이 발견되면, 해당 노드부터 군집을 찾기 시작

T = int(input())

cluster_counts = []

for t in range(T):
    cluster_count = 0
    M, N, K = map(int, input().split())
    
    baechu = [[0 for _ in range(N)] for _ in range(M)]

    # 배추 심기
    for _ in range(K):
        r, c = map(int, input().split())
        baechu[r][c] = 1
    
    visited = [[False for _ in range(N)] for _ in range(M)]
    adjacents = [(1,0),(-1,0),(0,1),(0,-1)]

    def search_cluster(r, c):
        queue = deque([(r, c)])
        visited[r][c] = True

        while queue:
            cur_r, cur_c = queue.popleft()
            for dr, dc in adjacents:
                new_r, new_c = cur_r + dr, cur_c + dc
                if 0 <= new_r < M and 0 <= new_c < N and not visited[new_r][new_c] and baechu[new_r][new_c] == 1:
                    visited[new_r][new_c] = True
                    queue.append((new_r, new_c))
    
    # 모든 노드를 순회하면서
    for r in range(M):
        for c in range(N):
            if baechu[r][c] == 1 and not visited[r][c]: # 새로운 배추 뭉탱이 찾기 시작
                search_cluster(r, c) # bfs 시작
                cluster_count += 1
    
    cluster_counts.append(cluster_count)

for c in cluster_counts:
    print(c)
