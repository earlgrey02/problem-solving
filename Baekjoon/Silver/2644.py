import sys
from collections import deque

input = sys.stdin.readline

def bfs(v: int) -> int:
    queue = deque([v])
    visited[v] = 0

    while queue:
        v = queue.popleft()

        if v == destination:
            return visited[v]

        for next_v in adjacencies[v]:
            if visited[next_v] == -1:
                visited[next_v] = visited[v] + 1
                queue.append(next_v)

    return -1

n = int(input())
v, destination = map(int, input().split())
m = int(input())
adjacencies = [[] for _ in range(n + 1)]
visited = [-1 for _ in range(n + 1)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    adjacencies[v1].append(v2)
    adjacencies[v2].append(v1)

print(bfs(v))