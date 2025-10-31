import sys
from collections import deque

input = sys.stdin.readline

def bfs(v: tuple[int, int, int]):
    queue = deque([v])
    visited[v[0]][v[1]][v[2]] = 0

    while queue:
        v = queue.popleft()

        if v[:2] == (h - 1, w - 1):
            return visited[v[0]][v[1]][v[2]]

        for i in range(12 if v[2] < k else 4):
            next_v = (v[0] + dy[i], v[1] + dx[i], v[2] if i < 4 else v[2] + 1)

            if 0 <= next_v[0] < h and 0 <= next_v[1] < w and matrix[next_v[0]][next_v[1]] == 0 and visited[next_v[0]][next_v[1]][next_v[2]] == -1:
                visited[next_v[0]][next_v[1]][next_v[2]] = visited[v[0]][v[1]][v[2]] + 1
                queue.append(next_v)

    return -1

k = int(input())
w, h = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(h)]
visited = [[[-1 for _ in range(k + 1)] for _ in range(w)] for _ in range(h)]
dy = (1, -1, 0, 0, -2, -1, 1, 2, 2, 1, -1, -2)
dx = (0, 0, 1, -1, 1, 2, 2, 1, -1, -2, -2, -1)

print(bfs((0, 0, 0)))