import sys
from itertools import groupby

input = sys.stdin.readline

s = input().strip()
groups = list(map(lambda x: int(x[0]), groupby(s)))

print(min(groups.count(i) for i in range(2)))