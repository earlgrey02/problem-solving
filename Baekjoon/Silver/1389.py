import sys
from math import inf

input = sys.stdin.readline

def floyd_warshall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

n, m = map(int, input().split())
distances = [[inf if i != j else 0 for j in range(n)] for i in range(n)]

for _ in range(m):
    v1, v2 = map(lambda x: int(x) - 1, input().split())
    distances[v1][v2] = distances[v2][v1] = 1

floyd_warshall()

print(min(enumerate(map(sum, distances)), key = lambda x: x[1])[0] + 1)