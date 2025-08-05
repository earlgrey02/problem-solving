import sys
from collections import deque
from math import inf

input = sys.stdin.readline

def topological_sort():
    queue = deque([i for i in range(n) if indegrees[i] == 0])

    while queue:
        v = queue.popleft()

        for next_v in adjacencies[v]:
            indegrees[next_v] -= 1
            dp[next_v] = max(dp[next_v], dp[v] + costs[next_v])

            if indegrees[next_v] == 0:
                queue.append(next_v)

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    costs = list(map(int, input().split()))
    adjacencies = [[] for _ in range(n)]
    indegrees = [0 for _ in range(n)]

    for _ in range(k):
        start, end = map(lambda x: int(x) - 1, input().split())
        adjacencies[start].append(end)
        indegrees[end] += 1

    w = int(input())
    dp = [costs[i] if indegrees[i] == 0 else -inf for i in range(n)]

    topological_sort()

    print(dp[w - 1])