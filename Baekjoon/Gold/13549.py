import sys
from heapq import heappop, heappush
from math import inf

input = sys.stdin.readline

def dijkstra(v: int):
    heap = [(0, v)]
    distances[v] = 0

    while heap:
        w, v = heappop(heap)

        if distances[v] < w:
            continue

        for next_v, next_w in ((v - 1, 1), (v + 1, 1), (v * 2, 0)):
            next_w += w

            if 0 <= next_v <= 100000 and next_w < distances[next_v]:
                distances[next_v] = next_w
                heappush(heap, (next_w, next_v))

n, k = map(int, input().split())
distances = [inf for _ in range(100001)]

dijkstra(n)

print(distances[k])