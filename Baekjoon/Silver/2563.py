import sys

input = sys.stdin.readline

n = int(input())
matrix = [[False for _ in range(101)] for _ in range(101)]

for _ in range(n):
    a, b = map(int, input().split())

    for i in range(a, a + 10):
        for j in range(b, b + 10):
            matrix[j][i] = True

print(len([True for i in range(101) for j in range(101) if matrix[i][j]]))