import sys
from math import inf

input = sys.stdin.readline

def floyd_warshall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if adjacencies[i][k] == 1 and adjacencies[k][j] == 1:
                    adjacencies[i][j] = 1

n = int(input())
adjacencies = [list(map(int, input().split())) for _ in range(n)]

floyd_warshall()

for row in adjacencies:
    print(*row)