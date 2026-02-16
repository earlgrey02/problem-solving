import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(v: int):
    for next_v in adjacencies[v]:
        if depths[next_v] == -1:
            depths[next_v] = depths[v] + 1
            parents[next_v][0] = v
            dfs(next_v)

def lca(v1: int, v2: int) -> int:
    if depths[v1] < depths[v2]:
        v1, v2 = v2, v1

    diff = depths[v1] - depths[v2]

    for i in range(log):
        if diff & (1 << i):
            v1 = parents[v1][i]

    if v1 == v2:
        return v1

    for i in range(log - 1, -1, -1):
        if parents[v1][i] != parents[v2][i]:
            v1, v2 = parents[v1][i], parents[v2][i]

    return parents[v1][0]

n = int(input())
adjacencies = [[] for _ in range(n)]
log = n.bit_length()
depths = [-1 if i > 0 else 0 for i in range(n)]
parents = [[0 for _ in range(log)] for _ in range(n)]

for _ in range(n - 1):
    v1, v2 = map(lambda x: int(x) - 1, input().split())
    adjacencies[v1].append(v2)
    adjacencies[v2].append(v1)

dfs(0)

for i in range(1, log):
    for j in range(n):
        parents[j][i] = parents[parents[j][i - 1]][i - 1]

m = int(input())

for _ in range(m):
    v1, v2 = map(lambda x: int(x) - 1, input().split())

    print(lca(v1, v2) + 1)