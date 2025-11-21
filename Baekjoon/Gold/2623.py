import sys
from collections import deque

input = sys.stdin.readline

def topological_sort() -> list[int]:
    queue = deque(i for i in range(n) if indegrees[i] == 0)
    order = []

    while queue:
        v = queue.popleft()
        order.append(v + 1)

        for next_v in adjacencies[v]:
            indegrees[next_v] -= 1

            if indegrees[next_v] == 0:
                queue.append(next_v)

    return order

n, m = map(int, input().split())
adjacencies = [[] for _ in range(n)]
indegrees = [0 for _ in range(n)]

for _ in range(m):
    for start, end in zip(order := list(map(lambda x: int(x) - 1, input().split()))[1:], order[1:]):
        adjacencies[start].append(end)
        indegrees[end] += 1

print(*order if len(order := topological_sort()) == n else [0], sep = '\n')