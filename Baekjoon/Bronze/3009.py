from itertools import product
import sys

input = sys.stdin.readline
points = {tuple(map(int, input().split())) for _ in range(3)}

print(*(set(product({point[0] for point in points}, {point[1] for point in points})) - points).pop())
