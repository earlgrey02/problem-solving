import sys

input = sys.stdin.readline

n = int(input())
points = list(map(int, input().split()))
compressed_points = {value: index for index, value in enumerate(sorted(set(points)))}

print(*(compressed_points[i] for i in points))