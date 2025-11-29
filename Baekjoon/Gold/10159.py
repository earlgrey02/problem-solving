import sys

input = sys.stdin.readline

def floyd_warshall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if adjacencies[i][k] == 1 and adjacencies[k][j] == 1:
                    adjacencies[i][j] = 1
                elif adjacencies[i][k] == -1 and adjacencies[k][j] == -1:
                    adjacencies[i][j] = -1

n, m = (int(input()) for _ in range(2))
adjacencies = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    start, end = map(int, input().split())
    adjacencies[start - 1][end - 1] = 1
    adjacencies[end - 1][start - 1] = -1

floyd_warshall()

print(*(adjacencies[i].count(0) - 1 for i in range(n)), sep = '\n')