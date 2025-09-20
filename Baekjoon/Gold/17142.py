import sys
from collections import deque
from itertools import combinations
from math import inf

input = sys.stdin.readline

def bfs(viruses: list[tuple[int, int]]):
    queue = deque(viruses)
    visited = [[0 if (i, j) in viruses else -1 for j in range(n)] for i in range(n)]
    time = 0

    while queue:
        v = queue.popleft()

        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if 0 <= next_v[0] < n and 0 <= next_v[1] < n and matrix[next_v[0]][next_v[1]] != 1 and visited[next_v[0]][next_v[1]] == -1:
                visited[next_v[0]][next_v[1]] = visited[v[0]][v[1]] + 1
                queue.append(next_v)

                if matrix[next_v[0]][next_v[1]] == 0:
                    time = max(time, visited[next_v[0]][next_v[1]])

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0 and visited[i][j] == -1:
                return -1

    return time

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
viruses = [(i, j) for i in range(n) for j in range(n) if matrix[i][j] == 2]
time = inf
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

for case in map(list, combinations(viruses, m)):
    if (temp := bfs(case)) > -1:
        time = min(time, temp)

print(time if time != inf else -1)