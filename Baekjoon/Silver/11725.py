import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(v: int):
    for next_v in adjacencies[v]:
        if visited[next_v] == -1:
            visited[next_v] = v
            dfs(next_v)

n = int(input())
adjacencies = [[] for _ in range(n + 1)]
visited = [-1 for _ in range(n + 1)]

for _ in range(n - 1):
    v1, v2 = map(int, input().split())
    adjacencies[v1].append(v2)
    adjacencies[v2].append(v1)

visited[1] = 0
dfs(1)

print(*visited[2:], sep = '\n')