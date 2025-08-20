import sys
from collections import deque

input = sys.stdin.readline

def bfs(v: int):
    queue = deque([v])
    visited[v] = [0, 1]

    while queue:
        v = queue.popleft()

        for next_v in (v - 1, v + 1, v * 2):
            if 0 <= next_v <= 100000:
                if visited[next_v][0] == -1:
                    visited[next_v][0] = visited[v][0] + 1
                    visited[next_v][1] = visited[v][1]
                    queue.append(next_v)
                elif visited[next_v][0] == visited[v][0] + 1:
                    visited[next_v][1] += visited[v][1]

n, k = map(int, input().split())
visited = [[-1, 0] for _ in range(100001)]

bfs(n)

print(*visited[k], sep = '\n')