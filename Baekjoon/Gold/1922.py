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

n, m = [int(input()) for _ in range(2)]
edges = sorted([tuple(map(int, input().split())) for _ in range(m)], key = lambda x: x[2])
parents = [i for i in range(n + 1)]
ranks = [0 for _ in range(n + 1)]

print(kruskal())