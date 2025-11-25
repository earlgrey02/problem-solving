import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
line = [int(input()) for _ in range(n)]
dp = [line[0]]

for i in range(n):
    if dp[-1] < line[i]:
        dp.append(line[i])
    else:
        dp[bisect_left(dp, line[i])] = line[i]

print(n - len(dp))