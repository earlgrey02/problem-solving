import sys
from collections import deque

input = sys.stdin.readline

def bfs(v: int):
    queue = deque([v])
    visited[v] = True
    orders[v] = (order := 1)

    while queue:
        v = queue.popleft()

        for next_v in adjacencies[v]:
            if not visited[next_v]:
                visited[next_v] = True
                orders[next_v] = (order := order + 1)
                queue.append(next_v)

n, m, r = map(int, input().split())
adjacencies = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
orders = [0 for _ in range(n + 1)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    adjacencies[v1].append(v2)
    adjacencies[v2].append(v1)

for i in range(n + 1):
    adjacencies[i].sort(reverse = True)

bfs(r)

print(*orders[1:], sep = '\n')