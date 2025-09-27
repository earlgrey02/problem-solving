import sys
from collections import deque

input = sys.stdin.readline

def bfs(v: tuple[int, int, int, int]) -> int:
    queue = deque([v])
    visited[v[0]][v[1]][v[2]] = True

    while queue:
        v = queue.popleft()

        if v[:2] == (n - 1, m - 1):
            return v[3]

        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if 0 <= next_v[0] < n and 0 <= next_v[1] < m:
                if matrix[next_v[0]][next_v[1]] == 1 and v[2] < k and not visited[next_v[0]][next_v[1]][v[2] + 1]:
                    if v[3] % 2 == 0:
                        queue.append((*v[:3], v[3] + 1))
                    else:
                        visited[next_v[0]][next_v[1]][v[2] + 1] = True
                        queue.append((*next_v[:2], v[2] + 1, v[3] + 1))
                elif matrix[next_v[0]][next_v[1]] == 0 and not visited[next_v[0]][next_v[1]][v[2]]:
                    visited[next_v[0]][next_v[1]][v[2]] = True
                    queue.append((*next_v[:2], v[2], v[3] + 1))

    return -1

n, m, k = map(int, input().split())
matrix = [list(map(int, input().strip())) for _ in range(n)]
visited = [[[False for _ in range(k + 1)] for _ in range(m)] for _ in range(n)]
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

print(bfs((0, 0, 0, 1)))