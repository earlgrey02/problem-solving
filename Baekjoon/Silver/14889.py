from math import inf
import sys

input = sys.stdin.readline

def dfs(depth: int, index: int):
    global minimum

    if depth == n // 2:
        start = sum(stats[i][j] for i in range(n) for j in range(n) if visited[i] and visited[j])
        link = sum(stats[i][j] for i in range(n) for j in range(n) if not (visited[i] or visited[j]))
        minimum = min(minimum, abs(start - link))
    else:
        for i in range(index, n):
            if not visited[i]:
                visited[i] = True
                dfs(depth + 1, i + 1)
                visited[i] = False

n = int(input())
stats = [list(map(int, input().split())) for _ in range(n)]
visited = [False for _ in range(n)]
minimum = inf

dfs(0, 0)

print(minimum)