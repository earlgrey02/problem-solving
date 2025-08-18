import sys
from collections import deque

input = sys.stdin.readline

def bfs(v: int) -> bool:
    queue = deque([v])
    visited[v] = 1

    while queue:
        v = queue.popleft()

        for next_v in adjacencies[v]:
            if visited[next_v] == 0:
                visited[next_v] = -visited[v]
                queue.append(next_v)
            elif visited[v] == visited[next_v]:
                return False

    return True

k = int(input())

for _ in range(k):
    v, e = map(int, input().split())
    adjacencies = [[] for _ in range(v + 1)]
    visited = [0 for _ in range(v + 1)]
    is_bipartite = True

    for _ in range(e):
        v1, v2 = map(int, input().split())
        adjacencies[v1].append(v2)
        adjacencies[v2].append(v1)

    for i in range(1, v + 1):
        if not visited[i] and not bfs(i):
            is_bipartite = False
            break

    print("YES" if is_bipartite else "NO")