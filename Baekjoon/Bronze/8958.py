import sys
from itertools import groupby

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    results = list(input().strip())
    score = 0

    for i, group in groupby(results):
        if i == "O":
            n = len(list(group))
            score += n * (n + 1) // 2

    print(score)