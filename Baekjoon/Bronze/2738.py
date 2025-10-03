import sys

input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

for row in matrix:
    print(*map(sum, zip(row, list(map(int, input().split())))))