import sys
from functools import reduce

input = sys.stdin.readline

n = int(input())
times = sorted(tuple(map(int, input().split())) for _ in range(n))

print(reduce(lambda acc, x: acc + x[1] if acc >= x[0] else sum(x), times, 0))