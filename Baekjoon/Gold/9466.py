import sys
from collections import deque

input = sys.stdin.readline

def topological_sort() -> int:
    queue = deque(i for i in range(n) if indegrees[i] == 0)
    count = len(queue)

    while queue:
        v = queue.popleft()
        next_v = adjacencies[v]
        indegrees[next_v] -= 1

        if indegrees[next_v] == 0:
            count += 1
            queue.append(next_v)

    return count

t = int(input())

for _ in range(t):
    n = int(input())
    adjacencies = list(map(lambda x: int(x) - 1, input().split()))
    indegrees = [0 for _ in range(n)]

    for v in adjacencies:
        indegrees[v] += 1

    print(topological_sort())