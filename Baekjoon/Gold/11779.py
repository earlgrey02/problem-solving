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

        for next_v, next_w in adjacencies[v]:
            next_w += w

            if next_w < distances[next_v]:
                prev[next_v] = v
                distances[next_v] = next_w
                heappush(heap, (next_w, next_v))

n, m = (int(input()) for _ in range(2))
adjacencies = [[] for _ in range(n + 1)]
distances = [inf for _ in range(n + 1)]
prev = [0 for _ in range(n + 1)]

for _ in range(m):
    start, end, w = map(int, input().split())
    adjacencies[start].append((end, w))

start, destination = map(int, input().split())

dijkstra(start)

path = [destination]
distance = distances[destination]

while (v := prev[destination]) != 0:
    path.append(destination := v)

print(distance)
print(len(path))
print(*path[::-1])