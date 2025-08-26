import sys
from math import inf

input = sys.stdin.readline

def dfs(v: int, visited: int) -> int | float:
    if visited == (1 << n) - 1:
        return adjacencies[v][0] if adjacencies[v][0] > 0 else inf
    elif (v, visited) in dp:
        return dp[(v, visited)]
    else:
        dp[(v, visited)] = inf

        for next_v, next_w in enumerate(adjacencies[v]):
            if next_w > 0 and not (visited & (1 << next_v)):
                dp[(v, visited)] = min(dp[(v, visited)], dfs(next_v, visited | (1 << next_v)) + next_w)

    return dp[(v, visited)]

n = int(input())
adjacencies = [list(map(int, input().split())) for _ in range(n)]
dp = {}

print(dfs(0, 1))