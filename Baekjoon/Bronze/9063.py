import sys

input = sys.stdin.readline

n = int(input())
x_points, y_points = zip(*(tuple(map(int, input().split())) for _ in range(n)))

print((max(x_points) - min(x_points)) * (max(y_points) - min(y_points)))