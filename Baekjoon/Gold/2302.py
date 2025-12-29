import sys
from functools import reduce

input = sys.stdin.readline

n, m = (int(input()) for _ in range(2))
seats = [0, *(int(input()) for _ in range(m)), n + 1]
intervals = [seats[i + 1] - seats[i] - 1 for i in range(len(seats) - 1)]
dp = [0 if i > 1 else 1 for i in range(max(intervals) + 1)]

for i in range(2, len(dp)):
    dp[i] = sum(dp[i - 2:i])

print(reduce(lambda acc, x: acc * dp[x], intervals, 1))