import heapq
import sys
from math import inf

input = sys.stdin.readline

def dijkstra(v):
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

v, e = map(int, input().split())
k = int(input())
adjacencies = [[] for _ in range(v + 1)]
distances = [inf for _ in range(v + 1)]

for _ in range(e):
    v1, v2, w = map(int, input().split())
    adjacencies[v1].append((v2, w))

dijkstra(k)

print(*(distances[i] if distances[i] != inf else "INF" for i in range(1, v + 1)), sep = "\n")