import sys
from math import comb
from collections import Counter

input = sys.stdin.readline

n, m = map(int, input().split())
sequence = list(map(int, input().split()))
prefix_sum = [0 for _ in range(n)]

for i in range(n):
    prefix_sum[i] = (sequence[i] + (prefix_sum[i - 1] if i > 0 else 0)) % m

counter = Counter(prefix_sum)

print(counter[0] + sum(map(lambda x: comb(x, 2), counter.values())))