import sys
from math import inf

input = sys.stdin.readline

def floyd_warshall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j]) if i != j else 0

n, m = [int(input()) for _ in range(2)]
distances = [[inf for _ in range(n)] for _ in range(n)]

for _ in range(m):
    start, end, w = map(int, input().split())
    distances[start - 1][end - 1] = min(distances[start - 1][end - 1], w)

floyd_warshall()

print(*(' '.join(map(str, (i if i != inf else 0 for i in row))) for row in distances), sep = '\n')