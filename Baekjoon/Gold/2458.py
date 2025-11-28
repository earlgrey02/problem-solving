import sys
from math import inf

input = sys.stdin.readline

def floyd_warshall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if adjacencies[i][k] == 1 and adjacencies[k][j] == 1:
                    adjacencies[i][j] = 1
                elif adjacencies[i][k] == -1 and adjacencies[k][j] == -1:
                    adjacencies[i][j] = -1

n, m = map(int, input().split())
adjacencies = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    start, end = map(int, input().split())
    adjacencies[start - 1][end - 1] = 1
    adjacencies[end - 1][start - 1] = -1

floyd_warshall()

print(sum(1 for row in adjacencies if row.count(0) == 1))