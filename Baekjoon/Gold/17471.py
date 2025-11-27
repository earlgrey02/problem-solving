import sys
from collections import deque
from itertools import combinations
from math import inf

input = sys.stdin.readline

def bfs(v: int, group: set[int]) -> bool:
    queue = deque([v])
    visited = [False for _ in range(n)]
    visited[v] = True

    while queue:
        v = queue.popleft()

        for next_v in adjacencies[v]:
            if next_v in group and not visited[next_v]:
                visited[next_v] = True
                queue.append(next_v)

    return group == {v for v in range(n) if visited[v]}

n = int(input())
populations = list(map(int, input().split()))
adjacencies = [set() for _ in range(n)]
diff = inf

for v1 in range(n):
    for v2 in list(map(lambda x: int(x) - 1, input().split()))[1:]:
        adjacencies[v1].add(v2)
        adjacencies[v2].add(v1)

for i in range(1, n):
    for case in combinations(range(n), i):
        groups = (group := set(case), set(range(n)) - group)

        if all(bfs(next(iter(group)), group) for group in groups):
            diff = min(diff, abs(sum(populations[v] for v in groups[0]) - sum(populations[v] for v in groups[1])))

print(diff if diff != inf else -1)