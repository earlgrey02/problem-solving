import sys
from math import inf

input = sys.stdin.readline

def floyd_warshall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

n, m, r = map(int, input().split())
items = list(map(int, input().split()))
distances = [[inf if i != j else 0 for j in range(n)] for i in range(n)]

for _ in range(r):
    v1, v2, w = map(int, input().split())
    distances[v1 - 1][v2 - 1] = w
    distances[v2 - 1][v1 - 1] = w

floyd_warshall()

print(max(sum(items[j] for j in range(n) if distances[i][j] <= m) for i in range(n)))