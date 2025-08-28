import sys
from math import inf

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    scores = sorted(tuple(map(int, input().split())) for _ in range(n))
    min_score = inf
    count = 0

    for i in range(n):
        if scores[i][1] < min_score:
            min_score = scores[i][1]
            count += 1

    print(count)