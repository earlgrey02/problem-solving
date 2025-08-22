import sys
from collections import deque

input = sys.stdin.readline

def bfs(v: int) -> int:
    queue = deque([v])
    visited[v] = 0

    while queue:
        v = queue.popleft()

        if v == 100:
            return visited[v]

        for i in range(1, 7):
            next_v = d[v + i] if v + i in d else v + i

            if 0 < next_v < 101 and visited[next_v] == -1:
                visited[next_v] = visited[v] + 1
                queue.append(next_v)

    return 0

n, m = map(int, input().split())
d = {i: j for i, j in (map(int, input().split()) for _ in range(n + m))}
visited = [-1 for _ in range(101)]

print(bfs(1))