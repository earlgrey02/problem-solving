import sys
from collections import deque

input = sys.stdin.readline

def bfs(v: int) -> int:
    queue = deque([v])
    visited[v] = 0

    while queue:
        v = queue.popleft()

        if v == g:
            return visited[v]

        for next_v in (v + u, v - d):
            if 0 < next_v <= f and visited[next_v] == -1:
                visited[next_v] = visited[v] + 1
                queue.append(next_v)

    return -1

f, s, g, u, d = map(int, input().split())
visited = [-1 for _ in range(f + 1)]

print(count if (count := bfs(s)) >= 0 else "use the stairs")