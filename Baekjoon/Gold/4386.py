import sys
from math import dist

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

def kruskal() -> float:
    distance = 0

    for v1, v2, w in edges:
        if find(v1) != find(v2):
            distance += w
            union(v1, v2)

    return distance

n = int(input())
stars = [tuple(map(float, input().split())) for _ in range(n)]
edges = sorted([(i, j, dist(stars[i], stars[j])) for i in range(n) for j in range(i + 1, n)], key = lambda x: x[2])
parents = [i for i in range(n)]
ranks = [0 for i in range(n)]

print(kruskal())