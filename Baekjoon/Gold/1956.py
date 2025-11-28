import sys
from math import inf

input = sys.stdin.readline

def floyd_warshall():
    for k in range(v):
        for i in range(v):
            for j in range(v):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

v, e = map(int, input().split())
distances = [[inf for _ in range(v)] for _ in range(v)]

for _ in range(e):
    start, end, w = map(int, input().split())
    distances[start - 1][end - 1] = w

floyd_warshall()

print(distance if (distance := min(distances[i][i] for i in range(v))) != inf else -1)