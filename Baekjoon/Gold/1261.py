import sys
from heapq import heappop, heappush
from math import inf

input = sys.stdin.readline

def dijkstra(v: tuple[int, int]):
    heap = [(0, v)]
    distances[v[0]][v[1]] = 0

    while heap:
        w, v = heappop(heap)

        if distances[v[0]][v[1]] < w:
            continue

        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if 0 <= next_v[0] < n and 0 <= next_v[1] < m:
                next_w = w + matrix[next_v[0]][next_v[1]]

                if next_w < distances[next_v[0]][next_v[1]]:
                    distances[next_v[0]][next_v[1]] = next_w
                    heappush(heap, (next_w, next_v))

m, n = map(int, input().split())
matrix = [list(map(int, input().strip())) for _ in range(n)]
distances = [[inf for _ in range(m)] for _ in range(n)]
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

dijkstra((0, 0))

print(distances[-1][-1])