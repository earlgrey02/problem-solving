import sys
from math import dist

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    planets = [tuple(map(int, input().split())) for _ in range(n)]
    count = 0

    for x3, y3, r in planets:
        d1, d2 = (dist(v, (x3, y3)) for v in ((x1, y1), (x2, y2)))

        if (d1 < r) ^ (d2 < r):
            count += 1

    print(count)