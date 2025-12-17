import sys
from math import inf

input = sys.stdin.readline

n, m = map(int, input().split())
sequence = sorted(int(input()) for _ in range(n))
left, right = 0, 0
min_difference = inf

while left <= right < n:
    if (difference := sequence[right] - sequence[left]) >= m:
        min_difference = min(min_difference, difference)
        left += 1
    else:
        right += 1

print(min_difference)