import sys
from heapq import heappop, heappush

input = sys.stdin.readline

def topological_sort():
    heap = sorted(i for i in range(1, n + 1) if indegrees[i] == 0)

    while heap:
        v = heappop(heap)

        print(v, end = ' ')

        for next_v in adjacencies[v]:
            indegrees[next_v] -= 1

            if indegrees[next_v] == 0:
                heappush(heap, next_v)

n, m = map(int, input().split())
adjacencies = [[] for i in range(n + 1)]
indegrees = [0 for i in range(n + 1)]

for _ in range(m):
    start, end = map(int, input().split())
    adjacencies[start].append(end)
    indegrees[end] += 1

topological_sort()