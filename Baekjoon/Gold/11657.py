import sys
from math import inf

input = sys.stdin.readline

def bellman_ford(v: int) -> bool:
    distances[v] = 0

    for i in range(n):
        for j in range(m):
            v, next_v, w = edges[j]

            if distances[v] != inf and distances[v] + w < distances[next_v]:
                if i == n - 1:
                    return False
                else:
                    distances[next_v] = distances[v] + w

    return True

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
distances = [inf for _ in range(n + 1)]

if bellman_ford(1):
    print(*(distances[i] if distances[i] != inf else -1 for i in range(2, n + 1)), sep = '\n')
else:
    print("-1")