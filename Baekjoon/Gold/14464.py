import sys
from bisect import bisect_left

input = sys.stdin.readline

c, n = map(int, input().split())
chickens = sorted(int(input()) for _ in range(c))
cows = sorted((tuple(map(int, input().split())) for _ in range(n)), key = lambda x: x[1])
count = 0

for start, end in cows:
    if (index := bisect_left(chickens, start)) < len(chickens) and chickens[index] <= end:
        count += 1
        chickens.pop(index)

print(count)