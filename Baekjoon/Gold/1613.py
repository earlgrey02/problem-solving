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

n, k = map(int, input().split())
adjacencies = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(k):
    start, end = map(int, input().split())
    adjacencies[start - 1][end - 1] = -1
    adjacencies[end - 1][start - 1] = 1

floyd_warshall()

s = int(input())

for _ in range(s):
    start, end = map(lambda x: int(x) - 1, input().split())

    print(adjacencies[start][end])