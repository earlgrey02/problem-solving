import sys
from collections import deque
from heapq import heappop, heappush
from math import inf

input = sys.stdin.readline

def dijkstra(v: int) -> list[float]:
    distances = [inf for _ in range(n + 1)]
    heap = [(0, v)]
    distances[v] = 0

    while heap:
        w, v = heappop(heap)

        if distances[v] < w:
            continue

        for next_v, next_w in adjacencies[0][v]:
            next_w += w

            if next_w < distances[next_v] and not visited[v][next_v]:
                distances[next_v] = next_w
                heappush(heap, (next_w, next_v))

    return distances

def bfs(v: int, distances: list[float]):
    queue = deque([v])

    while queue:
        v = queue.popleft()

        for next_v, next_w in adjacencies[1][v]:
            if distances[next_v] + next_w == distances[v] and not visited[next_v][v]:
                visited[next_v][v] = True
                queue.append(next_v)

while (line := tuple(map(int, input().split()))) != (0, 0):
    n, m = line
    s, d = map(int, input().split())
    adjacencies = [[[] for _ in range(n)] for _ in range(2)]
    visited = [[False for _ in range(n)] for _ in range(n)]

    for _ in range(m):
        start, end, w = map(int, input().split())
        adjacencies[0][start].append((end, w))
        adjacencies[1][end].append((start, w))

    bfs(d, dijkstra(s))

    print(distance if (distance := dijkstra(s)[d]) != inf else -1)