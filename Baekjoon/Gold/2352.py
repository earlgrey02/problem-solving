import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
ports = list(map(int, input().split()))
dp = [ports[0]]

for i in range(n):
    if dp[-1] < ports[i]:
        dp.append(ports[i])
    else:
        dp[bisect_left(dp, ports[i])] = ports[i]

print(len(dp))