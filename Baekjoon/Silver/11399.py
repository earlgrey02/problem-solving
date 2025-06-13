import sys
from itertools import accumulate

input = sys.stdin.readline

n = int(input())
times = sorted(list(map(int, input().split())))

print(sum(accumulate(times)))