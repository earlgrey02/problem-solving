import sys
from itertools import accumulate

input = sys.stdin.readline

n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
events = sorted((line[i], 1 if i == 0 else -1) for i in range(2) for line in lines)

print(max(accumulate(event[1] for event in events)))