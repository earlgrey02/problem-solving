import sys
from heapq import heappop, heappush
from math import inf

input = sys.stdin.readline

def dijkstra(v: int) -> list[int | float]:
    distances = [inf for _ in range(n + 1)]
    heap = [(0, v)]
    distances[v] = 0

    while heap:
        w, v = heappop(heap)

        if distances[v] < w:
            continue

        for next_v, next_w in adjacencies[v]:
            next_w += w

            if next_w < distances[next_v]:
                distances[next_v] = next_w
                heappush(heap, (next_w, next_v))

    return distances

n, e = map(int, input().split())
adjacencies = [[] for _ in range(n + 1)]

for _ in range(e):
    v1, v2, w = map(int, input().split())
    adjacencies[v1].append((v2, w))
    adjacencies[v2].append((v1, w))

v1, v2 = map(int, input().split())
answer = min(sum(dijkstra(i)[j] for i, j in zip(path, path[1:])) for path in ((1, v1, v2, n), (1, v2, v1, n)))

print(answer if answer != inf else -1)