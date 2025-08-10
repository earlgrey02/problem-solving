import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

def dfs(v: int, visited: list[bool]):
    print(v, end = " ")
    visited[v] = True

    for next_v in adjacencies[v]:
        if not visited[next_v]:
            dfs(next_v, visited)

def bfs(v: int, visited: list[bool]):
    queue = deque([v])
    visited[v] = True

    while queue:
        v = queue.popleft()
        print(v, end = " ")

        for next_v in adjacencies[v]:
            if not visited[next_v]:
                visited[next_v] = True
                queue.append(next_v)

n, m, v = map(int, input().split())
adjacencies = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    adjacencies[v1].append(v2)
    adjacencies[v2].append(v1)

for i in range(n + 1):
    adjacencies[i].sort()

dfs(v, deepcopy(visited))
print()
bfs(v, deepcopy(visited))