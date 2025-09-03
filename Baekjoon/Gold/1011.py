import sys
from math import isqrt

input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    x, y = map(int, input().split())
    d = y - x
    k = isqrt(d)

    if k ** 2 == d:
        print(k * 2 - 1)
    elif d <= k ** 2 + k:
        print(k * 2)
    else:
        print(k * 2 + 1)