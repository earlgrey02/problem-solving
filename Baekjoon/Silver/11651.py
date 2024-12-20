import sys

input = sys.stdin.readline

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

print(*(f"{x} {y}" for x, y in sorted(points, key = lambda x: (x[1], x[0]))), sep = '\n')