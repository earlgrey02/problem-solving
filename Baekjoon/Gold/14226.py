import sys
from collections import deque

input = sys.stdin.readline

def bfs(v: tuple[int, int]) -> int:
    queue = deque([v])
    visited[v] = 0

    while queue:
        v = queue.popleft()

        if v[0] == s:
            return visited[v]

        for next_v in ((v[0], v[0]), (sum(v), v[1]), (v[0] - 1, v[1])):
            if next_v not in visited:
                visited[next_v] = visited[v] + 1
                queue.append(next_v)

    return -1

s = int(input())
visited = {}

print(bfs((1, 0)))