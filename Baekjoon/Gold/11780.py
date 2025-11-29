import sys
from math import inf

input = sys.stdin.readline

def floyd_warshall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distances[i][k] + distances[k][j] < distances[i][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
                    paths[i][j] = paths[i][k] + paths[k][j][1:]

n, m = (int(input()) for _ in range(2))
distances = [[inf if i != j else 0 for j in range(n)] for i in range(n)]
paths = [[() for _ in range(n)] for _ in range(n)]

for _ in range(m):
    start, end, w = map(int, input().split())
    distances[start - 1][end - 1] = min(distances[start - 1][end - 1], w)
    paths[start - 1][end - 1] = (start - 1, end - 1)

floyd_warshall()

for i in range(n):
    print(*map(lambda x: x if x != inf else 0, distances[i]))

for i in range(n):
    for j in range(n):
        print(len(paths[i][j]), *map(lambda x: x + 1, paths[i][j]))