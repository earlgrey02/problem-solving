import sys
from collections import deque

input = sys.stdin.readline

def bfs(v: int):
    queue = deque([v])
    visited[v] = 0

    while queue:
        v = queue.popleft()

        for next_v in adjacencies[v]:
            if visited[next_v] == -1:
                visited[next_v] = visited[v] + 1
                queue.append(next_v)

n, m, k, x = map(int, input().split())
adjacencies = [[] for _ in range(n + 1)]
visited = [-1 for _ in range(n + 1)]

for _ in range(m):
    start, end = map(int, input().split())
    adjacencies[start].append(end)

bfs(x)

if nodes := [i for i in range(1, n + 1) if visited[i] == k]:
    print(*nodes, sep = '\n')
else:
    print(-1)