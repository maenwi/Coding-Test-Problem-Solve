# 덩어리의 모든 좌표들을 key로 갖는 딕셔너리를 만들어서
# 해당 위치에 석유 시추 될 때 딕셔너리에서 검색해서 가져오게 하면 될듯?
# 좀 더 효율적으로 하려면, 덩어리의 가장 맨 위 좌표들만 key로,
# 그리고 그 덩어리의 크기를 value로

from collections import deque
from collections import defaultdict

def solution(land):
    R = len(land)
    C = len(land[0])
    visited = [[False] * C for _ in range(R)]
    d = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
    
    clusters = {}
    
    for r in range(R):
        for c in range(C):
            if land[r][c] == 1 and not visited[r][c]:
                # Cluster 찾기 시작
                q = deque([(r, c)])
                visited[r][c] = True
                a_cluster = [(r, c)]
                
                while q:
                    cr, cc = q.popleft()
                    
                    for dr, dc in d:
                        nr, nc = cr + dr, cc + dc
                        
                        if (0 <= nr < R and 
                            0 <= nc < C and 
                            land[nr][nc] == 1 and 
                            not visited[nr][nc]):
                            q.append((nr, nc))
                            visited[nr][nc] = True
                            a_cluster.append((nr, nc))
                    
                # cluster의 각 column 별로 row 값이 제일 작은거 뽑기
                a_cluster_ceil = defaultdict(lambda:R)
                for cluster_r, cluster_c in a_cluster:
                    # 현재 가장 높은 위치와 이번의 위치를 비교해서 작은 값만 남기기
                    a_cluster_ceil[cluster_c] = min(cluster_r, a_cluster_ceil[cluster_c])
                
                for cluster_c, cluster_r in a_cluster_ceil.items():
                    clusters[(cluster_r, cluster_c)] = len(a_cluster)
    
    # 여기서부터 이제 시추관 서치
    max_oils = -1
    for c in range(C):
        oils = 0
        for r in range(R):
            oils += clusters.get((r, c), 0)
        max_oils = max(oils, max_oils)
    
    return max_oils