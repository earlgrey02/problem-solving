import sys
from heapq import heappop, heappush
from math import inf

input = sys.stdin.readline

def dijkstra(v: int):
    heap = [(0, v)]
    distances[v][-1] = 0

    while heap:
        w, v = heappop(heap)

        if -distances[v][0] < w:
            continue

        for next_v, next_w in adjacencies[v]:
            next_w += w

            if next_w < -distances[next_v][0]:
                heappop(distances[next_v])
                heappush(distances[next_v], -next_w)
                heappush(heap, (next_w, next_v))

n, m, k = map(int, input().split())
adjacencies = [[] for _ in range(n + 1)]
distances = [[-inf for _ in range(k)] for _ in range(n + 1)]

for _ in range(m):
    start, end, w = map(int, input().split())
    adjacencies[start].append((end, w))

dijkstra(1)

print(*(distance if (distance := -distances[i][0]) != inf else -1 for i in range(1, n + 1)), sep = '\n')