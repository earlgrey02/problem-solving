import sys
from collections import deque

input = sys.stdin.readline

def bfs(v: int):
    queue = deque([v])
    visited[v] = 0

    while queue:
        v = queue.popleft()

        if v == k:
            return visited[v]

        for next_v in (v + 1, v - 1, v * 2):
            if 0 <= next_v <= 100_000 and visited[next_v] == -1:
                visited[next_v] = visited[v] + 1
                queue.append(next_v)

n, k = map(int, input().split())
visited = [-1 for _ in range(100_001)]

print(bfs(n))