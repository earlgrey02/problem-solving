import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
sequence = list(map(int, input().split()))
dp = [sequence[0]]

for i in range(n):
    if dp[-1] < sequence[i]:
        dp.append(sequence[i])
    else:
        dp[bisect_left(dp, sequence[i])] = sequence[i]

print(len(dp))