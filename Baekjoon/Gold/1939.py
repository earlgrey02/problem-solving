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
    for v1, v2, w in edges:
        if find(v1) != find(v2):
            union(v1, v2)

        if find(start) == find(destination):
            return w

    return 0

n, m = map(int, input().split())
edges = sorted(((v1 - 1, v2 - 1, w) for _ in range(m) for v1, v2, w in (map(int, input().split()),)), key = lambda x: -x[2])
start, destination = map(lambda x: int(x) - 1, input().split())
parents = [i for i in range(n)]
ranks = [0 for _ in range(n)]

print(kruskal())