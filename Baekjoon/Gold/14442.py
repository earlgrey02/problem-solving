import sys
from collections import deque

input = sys.stdin.readline

def bfs(v: tuple[int, int, int]) -> int:
    queue = deque([v])
    visited[v[0]][v[1]] = 0

    while queue:
        v = queue.popleft()

        if v[:2] == (n - 1, m - 1):
            return v[2]

        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if 0 <= next_v[0] < n and 0 <= next_v[1] < m and (broken_count := visited[v[0]][v[1]] + matrix[next_v[0]][next_v[1]]) <= k and broken_count < visited[next_v[0]][next_v[1]]:
                visited[next_v[0]][next_v[1]] = broken_count
                queue.append((*next_v, v[2] + 1))

    return -1

n, m, k = map(int, input().split())
matrix = [list(map(int, input().strip())) for _ in range(n)]
visited = [[k + 1 for _ in range(m)] for _ in range(n)]
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

print(bfs((0, 0, 1)))