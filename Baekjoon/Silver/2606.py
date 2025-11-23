import sys

input = sys.stdin.readline

def find(v: int) -> int:
    if parents[v] != v:
        parents[v] = find(parents[v])

    return parents[v]

def union(v1: int, v2: int):
    v1, v2 = find(v1), find(v2)

    if v1 != v2:
        if ranks[v2] == ranks[v1]:
            parents[v2] = v1
            ranks[v1] += 1
        elif ranks[v1] < ranks[v2]:
            parents[v1] = v2
        else:
            parents[v2] = v1

n, m = [int(input()) for _ in range(2)]
parents = [i for i in range(n + 1)]
ranks = [0 for _ in range(n + 1)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    union(v1, v2)

print(sum(i for i in range(2, n + 1) if find(i) == find(1)))