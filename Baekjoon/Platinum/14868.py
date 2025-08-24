import sys
from collections import deque

input = sys.stdin.readline

def union(v1: int, v2: int):
    v1, v2 = find(v1), find(v2)

    if v1 != v2:
        if ranks[v1] == ranks[v2]:
            parents[v2] = v1
            ranks[v1] += 1
        elif ranks[v1] < ranks[v2]:
            parents[v1] = v2
        else:
            parents[v2] = v1

def find(v: int) -> int:
    if parents[v] != v:
        parents[v] = find(parents[v])

    return parents[v]

def merge_civils(civils: deque[tuple[int, int]]) -> int:
    count = 0

    for v in civils:
        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if 0 <= next_v[0] < n and 0 <= next_v[1] < n and matrix[next_v[0]][next_v[1]] > 0 and find(matrix[v[0]][v[1]]) != find(matrix[next_v[0]][next_v[1]]):
                union(matrix[v[0]][v[1]], matrix[next_v[0]][next_v[1]])
                count += 1

    return count

def civilization_bfs(civils: deque[tuple[int, int]]) -> deque[tuple[int, int]]:
    new_civils = deque()

    for _ in range(len(civils)):
        v = civils.popleft()

        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if 0 <= next_v[0] < n and 0 <= next_v[1] < n and matrix[next_v[0]][next_v[1]] == 0:
                matrix[next_v[0]][next_v[1]] = matrix[v[0]][v[1]]
                new_civils.append(next_v)

    return new_civils

n, k = map(int, input().split())
matrix = [[0 for _ in range(n)] for _ in range(n)]
civils = deque()
parents = [i for i in range(k + 1)]
ranks = [0 for _ in range(k + 1)]
year = 0
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

for i in range(k):
    y, x = map(lambda x: int(x) - 1, input().split())
    matrix[y][x] = i + 1
    civils.append((y, x))

while k > 1:
    if (k := k - merge_civils(civils)) == 1:
        break

    civils = civilization_bfs(civils)
    year += 1

print(year)