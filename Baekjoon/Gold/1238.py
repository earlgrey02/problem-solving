import sys
from heapq import heappop, heappush
from math import inf

input = sys.stdin.readline

def dijkstra(v: int, adjacencies: list[list[tuple[int, int]]]) -> list[float]:
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

n, m, x = map(int, input().split())
adjacencies = [[[] for _ in range(n + 1)] for _ in range(2)]

for _ in range(m):
    start, end, w = map(int, input().split())
    adjacencies[0][start].append((end, w))
    adjacencies[1][end].append((start, w))

distances = [dijkstra(x, adjacencies[i]) for i in range(2)]

print(max(distances[0][i] + distances[1][i] for i in range(1, n + 1) if i != x))