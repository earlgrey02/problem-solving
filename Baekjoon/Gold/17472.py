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

def kruskal() -> int:
    distance = 0

    for v1, v2, w in bridges:
        if find(v1) != find(v2):
            distance += w
            union(v1, v2)

    return distance

def flood_fill(v: tuple[int, int], label: int):
    queue = deque([v])
    label_visited[v[0]][v[1]] = True
    matrix[v[0]][v[1]] = label

    while queue:
        v = queue.popleft()

        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if 0 <= next_v[0] < n and 0 <= next_v[1] < m and not label_visited[next_v[0]][next_v[1]]:
                if matrix[next_v[0]][next_v[1]] == 0:
                    edges[label].add((*v, i))
                else:
                    label_visited[next_v[0]][next_v[1]] = True
                    matrix[next_v[0]][next_v[1]] = label
                    queue.append(next_v)

def get_bridges(edges: set[tuple[int, int, int]], label: int) -> set[tuple[int, int, int]]:
    queue = deque(edges)
    visited = [[[0 if (i, j, k) in edges else -1 for k in range(4)] for j in range(m)] for i in range(n)]
    bridges = set()

    while queue:
        v = queue.popleft()
        next_v = (v[0] + dy[v[2]], v[1] + dx[v[2]], v[2])

        if 0 <= next_v[0] < n and 0 <= next_v[1] < m and visited[next_v[0]][next_v[1]][next_v[2]] == -1:
            if matrix[next_v[0]][next_v[1]] == 0:
                visited[next_v[0]][next_v[1]][next_v[2]] = visited[v[0]][v[1]][v[2]] + 1
                queue.append(next_v)
            elif matrix[next_v[0]][next_v[1]] != label and visited[v[0]][v[1]][v[2]] >= 2:
                bridges.add((label, matrix[next_v[0]][next_v[1]], visited[v[0]][v[1]][v[2]]))

    return bridges

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
label_visited = [[False for _ in range(m)] for _ in range(n)]
edges = {}
bridges = set()
label = 1
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

for i in range(n):
    for j in range(m):
        if matrix[i][j] != 0 and not label_visited[i][j]:
            edges[label] = set()
            flood_fill((i, j), label)
            label += 1

parents = [i for i in range(label)]
ranks = [0 for _ in range(label)]

for i in range(1, label):
    bridges.update(get_bridges(edges[i], i))

bridges = sorted(bridges, key = lambda x: x[2])
distance = kruskal()

print(distance if all(find(i) == find(1) for i in range(1, label)) else -1)