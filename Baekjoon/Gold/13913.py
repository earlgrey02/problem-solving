import sys
from collections import defaultdict, deque

input = sys.stdin.readline

def bfs(v: int):
    queue = deque([v])
    visited[v] = v

    while queue:
        v = queue.popleft()

        if v == k:
            return

        for next_v in (v + 1, v - 1, v * 2):
            if 0 <= next_v <= 100000 and visited[next_v] == -1:
                visited[next_v] = v
                queue.append(next_v)

n, k = map(int, input().split())
visited = [-1 for _ in range(100001)]
path = [k]

bfs(n)

while (v := visited[k]) != k:
    path.append(k := v)

print(len(path) - 1)
print(*path[::-1])