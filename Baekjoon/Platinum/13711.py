import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
a, b = (list(map(int, input().split())) for _ in range(2))
indexes = {j: i for i, j in enumerate(b)}
sequence = [indexes[i] for i in a]
dp = [sequence[0]]

for i in range(n):
    if dp[-1] < sequence[i]:
        dp.append(sequence[i])
    else:
        dp[index := bisect_left(dp, sequence[i])] = sequence[i]

print(len(dp))