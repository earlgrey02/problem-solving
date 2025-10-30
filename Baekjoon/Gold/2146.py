import sys
from collections import deque
from math import inf

input = sys.stdin.readline

def index_bfs(v: tuple[int, int], visited: list[list[bool]], index: int):
    queue = deque([v])
    visited[v[0]][v[1]] = True
    matrix[v[0]][v[1]] = index

    while queue:
        v = queue.popleft()

        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if 0 <= next_v[0] < n and 0 <= next_v[1] < n and not visited[next_v[0]][next_v[1]]:
                if matrix[next_v[0]][next_v[1]] == 0:
                    edges[index].add(v)
                else:
                    visited[next_v[0]][next_v[1]] = True
                    matrix[next_v[0]][next_v[1]] = index
                    queue.append(next_v)

def bridge_bfs(edges: set[tuple[int, int]], index: int) -> float:
    queue = deque(edges)
    visited = [[0 if (i, j) in edges else -1 for j in range(n)] for i in range(n)]

    while queue:
        v = queue.popleft()

        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if 0 <= next_v[0] < n and 0 <= next_v[1] < n and visited[next_v[0]][next_v[1]] == -1:
                if matrix[next_v[0]][next_v[1]] == 0:
                    visited[next_v[0]][next_v[1]] = visited[v[0]][v[1]] + 1
                    queue.append(next_v)
                elif matrix[next_v[0]][next_v[1]] != index:
                    return visited[v[0]][v[1]]

    return inf

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
index_visited = [[False for _ in range(n)] for _ in range(n)]
edges = {}
index = 1
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

for i in range(n):
    for j in range(n):
        if matrix[i][j] != 0 and not index_visited[i][j]:
            edges[index] = set()
            index_bfs((i, j), index_visited, index)
            index += 1

print(min(bridge_bfs(edges[i], i) for i in range(1, index)))