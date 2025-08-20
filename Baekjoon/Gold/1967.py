import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(v: int, visited: list[int]):
    for next_v, next_w in adjacencies[v]:
        if visited[next_v] == -1:
            visited[next_v] = visited[v] + next_w
            dfs(next_v, visited)

n = int(input())
adjacencies = [[] for _ in range(n + 1)]
visited = [[-1 for _ in range(n + 1)] for _ in range(2)]

for _ in range(n - 1):
    v1, v2, w = map(int, input().split())
    adjacencies[v1].append((v2, w))
    adjacencies[v2].append((v1, w))

visited[0][1] = 0
dfs(1, visited[0])

visited[1][v := visited[0].index(max(visited[0]))] = 0
dfs(v, visited[1])

print(max(visited[1]))