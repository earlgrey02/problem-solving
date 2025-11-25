import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
lines = list(map(int, input().split()))
dp = [lines[0]]

for i in range(n):
    if dp[-1] < lines[i]:
        dp.append(lines[i])
    else:
        dp[bisect_left(dp, lines[i])] = lines[i]

print(n - len(dp))