import sys
from math import dist

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = dist((x1, y1), (x2, y2))

    if distance == 0 and r1 == r2:
        print(-1)
    elif distance == r1 + r2 or distance == abs(r1 - r2):
        print(1)
    elif distance > r1 + r2 or distance < abs(r1 - r2):
        print(0)
    else:
        print(2)