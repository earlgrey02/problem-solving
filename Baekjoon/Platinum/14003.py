import sys
from bisect import bisect_left
from collections import deque

input = sys.stdin.readline

n = int(input())
sequence = list(map(int, input().split()))
dp = [sequence[0]]
positions = [0 for _ in range(n)]
subsequence = deque()

for i in range(n):
    if dp[-1] < sequence[i]:
        dp.append(sequence[i])
        positions[i] = len(dp) - 1
    else:
        dp[index := bisect_left(dp, sequence[i])] = sequence[i]
        positions[i] = index

index = len(dp) - 1

for i in range(n - 1, -1, -1):
    if positions[i] == index:
        subsequence.appendleft(sequence[i])
        index -= 1

print(len(dp))
print(*subsequence)