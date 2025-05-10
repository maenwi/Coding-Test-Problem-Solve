import sys

input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(N-1):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

from collections import deque

queue = deque([1])
visited = [False] * (N + 1)
parents = [0] * (N + 1)

while queue:
    current = queue.popleft()
    visited[current] = True

    for adjacent in graph[current]:
        if not visited[adjacent]:
            queue.append(adjacent)
            parents[adjacent] = str(current)

print("\n".join(parents[2:]))