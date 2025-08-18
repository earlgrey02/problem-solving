import heapq
import sys
from math import inf

input = sys.stdin.readline

def dijkstra(v: int):
    heap = [(0, v)]
    distances[v] = 0

    while heap:
        w, v = heapq.heappop(heap)

        if distances[v] < w:
            continue

        for next_v, next_w in adjacencies[v]:
            next_w += w

            if next_w < distances[next_v]:
                distances[next_v] = next_w
                heapq.heappush(heap, (next_w, next_v))

n, m = [int(input()) for _ in range(2)]
adjacencies = [[] for _ in range(n + 1)]
distances = [inf for _ in range(n + 1)]

for _ in range(m):
    start, end, w = map(int, input().split())
    adjacencies[start].append((end, w))

v, destination = map(int, input().split())

dijkstra(v)

print(distances[destination])