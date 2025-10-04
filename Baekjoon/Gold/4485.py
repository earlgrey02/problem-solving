import sys
from heapq import heappop, heappush
from math import inf

input = sys.stdin.readline

def dijkstra(v: tuple[int, int]):
    heap = [(matrix[v[0]][v[1]], v)]
    distances[v[0]][v[1]] = matrix[v[0]][v[1]]

    while heap:
        w, v = heappop(heap)

        if distances[v[0]][v[1]] < w:
            continue

        for i in range(4):
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if 0 <= next_v[0] < n and 0 <= next_v[1] < n:
                next_w = w + matrix[next_v[0]][next_v[1]]

                if next_w < distances[next_v[0]][next_v[1]]:
                    distances[next_v[0]][next_v[1]] = next_w
                    heappush(heap, (next_w, next_v))

dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)
i = 1

while (n := int(input())) != 0:
    matrix = [list(map(int, input().split())) for _ in range(n)]
    distances = [[inf for _ in range(n)] for _ in range(n)]

    dijkstra((0, 0))

    print(f"Problem {i}: {distances[-1][-1]}")
    i += 1