import sys

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

    for v1, v2, w in edges:
        if find(v1) != find(v2):
            distance += w
            union(v1, v2)

    return distance

n = int(input())
planets = [tuple(map(int, input().split())) for _ in range(n)]
positions = [sorted(list(map(lambda x: (x[0], x[1][i]), enumerate(planets))), key = lambda x: x[1]) for i in range(3)]
edges = []
parents = [i for i in range(n + 1)]
ranks = [0 for _ in range(n + 1)]

for i in range(3):
    for j in range(n - 1):
        v1, v2, w = positions[i][j][0], positions[i][j + 1][0], abs(positions[i][j][1] - positions[i][j + 1][1])
        edges.append((v1, v2, w))

edges.sort(key = lambda x: x[2])

print(kruskal())