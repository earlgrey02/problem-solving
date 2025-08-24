import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(v: int):
    global order

    visited[v] = True
    orders[v] = (order := order + 1)

    for next_v in adjacencies[v]:
        if not visited[next_v]:
            dfs(next_v)

n, m, r = map(int, input().split())
adjacencies = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
orders = [0 for _ in range(n + 1)]
order = 0

for _ in range(m):
    v1, v2 = map(int, input().split())
    adjacencies[v1].append(v2)
    adjacencies[v2].append(v1)

for i in range(n + 1):
    adjacencies[i].sort()

dfs(r)

print(*orders[1:], sep = '\n')