import sys
from collections import deque
from math import inf

input = sys.stdin.readline

def topological_sort():
    queue = deque(i for i in range(n) if indegrees[i] == 0)

    while queue:
        v = queue.popleft()

        for next_v in adjacencies[v]:
            indegrees[next_v] -= 1
            dp[next_v] = max(dp[next_v], dp[v] + times[next_v])

            if indegrees[next_v] == 0:
                queue.append(next_v)

n = int(input())
adjacencies = [[] for _ in range(n)]
indegrees = [0 for _ in range(n)]
times = [0 for _ in range(n)]

for end in range(n):
    time, *starts, _ = map(int, input().split())

    for start in map(lambda x: x - 1, starts):
        adjacencies[start].append(end)
        indegrees[end] += 1

    times[end] = time

dp = [-inf if indegrees[i] > 0 else times[i] for i in range(n)]

topological_sort()

print(*dp, sep = '\n')