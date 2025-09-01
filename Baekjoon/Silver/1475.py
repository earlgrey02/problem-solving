import sys
from collections import Counter
from math import ceil

input = sys.stdin.readline

n = map(lambda x: int(x) if x != '9' else 6, input().strip())
counter = Counter(n)
counter[6] = ceil(counter[6] / 2)

print(max(counter.values()))