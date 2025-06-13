import sys
from itertools import accumulate

input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum = [0, *accumulate(numbers)]

for _ in range(m):
    i, j = map(int, input().split())

    print(prefix_sum[j] - prefix_sum[i - 1])