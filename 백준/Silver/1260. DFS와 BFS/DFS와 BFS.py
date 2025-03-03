N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)] # 노드 개수만큼

for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

for idx in range(len(graph)):
    graph[idx].sort()

from collections import deque

def bfs(v, graph):
    bfs_visit_nodes = []

    visited_bfs = [False for _ in range(N + 1)]

    # 시작 세팅
    queue = deque([v])
    visited_bfs[v] = True
    bfs_visit_nodes.append(str(v))

    while queue:
        current = queue.popleft()

        for adjacent_node in graph[current]:
            if not visited_bfs[adjacent_node]: # 아직 방문하지 않았다면
                queue.append(adjacent_node)
                visited_bfs[adjacent_node] = True
                bfs_visit_nodes.append(str(adjacent_node))
    
    return bfs_visit_nodes

def dfs(v, graph, visited_dfs = None, dfs_visit_nodes = None):
    if visited_dfs is None:
        visited_dfs = [False for _ in range(N + 1)]
    if dfs_visit_nodes is None:
        dfs_visit_nodes = []

    visited_dfs[v] = True
    dfs_visit_nodes.append(str(v))

    for adjacent_node in graph[v]:
        if not visited_dfs[adjacent_node]: # 아직 방문하지 않았다면,
            dfs(adjacent_node, graph, visited_dfs, dfs_visit_nodes)

    return dfs_visit_nodes

print(" ".join(dfs(V, graph)))
print(" ".join(bfs(V, graph)))