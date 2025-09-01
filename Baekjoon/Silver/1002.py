import sys
from math import hypot

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = hypot(x1 - x2, y1 - y2)

    if d == 0 and r1 == r2:
        print(-1)
    elif d == r1 + r2 or d == abs(r1 - r2):
        print(1)
    elif d > r1 + r2 or d < abs(r1 - r2):
        print(0)
    else:
        print(2)