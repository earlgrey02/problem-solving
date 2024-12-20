import sys

input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

for row_1 in matrix:
    row_2 = map(int, input().split())

    print(*map(sum, zip(row_1, row_2)))