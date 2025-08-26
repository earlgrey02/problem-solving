import sys
from math import dist, inf

input = sys.stdin.readline

def dfs(v: int, visited: int) -> float:
    if visited == (1 << n) - 1:
        return dist(cities[v], cities[0])
    elif (v, visited) in dp:
        return dp[(v, visited)]
    else:
        dp[(v, visited)] = inf

        for next_v in range(n):
            if not (visited & (1 << next_v)):
                dp[(v, visited)] = min(dp[(v, visited)], dfs(next_v, visited | (1 << next_v)) + dist(cities[next_v], cities[v]))

    return dp[(v, visited)]

n = int(input())
cities = [tuple(map(int, input().split())) for _ in range(n)]
dp = {}

print(dfs(0, 1))