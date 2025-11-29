import sys
from collections import deque

input = sys.stdin.readline

def topological_sort():
    queue = deque(i for i in range(n) if indegrees[i] == 0)

    while queue:
        v = queue.popleft()
        next_v = adjacencies[v]
        indegrees[next_v] -= 1

        if indegrees[next_v] == 0:
            queue.append(next_v)

n = int(input())
adjacencies = [int(input()) - 1 for _ in range(n)]
indegrees = [0 for _ in range(n)]

for v in adjacencies:
    indegrees[v] += 1

topological_sort()

print(len(numbers := [i + 1 for i in range(n) if indegrees[i] > 0]), *numbers, sep = '\n')