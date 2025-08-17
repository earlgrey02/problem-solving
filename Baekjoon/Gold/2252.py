import sys
from collections import deque

input = sys.stdin.readline

def topological_sort():
    queue = deque(i for i in range(n) if indegrees[i] == 0)

    while queue:
        v = queue.popleft()

        print(v + 1, end = ' ')

        for next_v in adjacencies[v]:
            indegrees[next_v] -= 1

            if indegrees[next_v] == 0:
                queue.append(next_v)

n, m = map(int, input().split())
adjacencies = [[] for _ in range(n)]
indegrees = [0 for _ in range(n)]

for _ in range(m):
    start, end = map(lambda x: int(x) - 1, input().split())
    adjacencies[start].append(end)
    indegrees[end] += 1

topological_sort()