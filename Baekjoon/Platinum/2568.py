import sys
from bisect import bisect_left
from collections import deque

input = sys.stdin.readline

n = int(input())
lines = sorted((tuple(map(int, input().split())) for _ in range(n)), key = lambda x: x[0])
sequence = list(map(lambda x: x[1], lines))
dp = [sequence[0]]
positions = [0 for _ in range(n)]
subsequence = set()

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
        subsequence.add(sequence[i])
        index -= 1

print(n - len(dp))
print(*(i for i, j in lines if j not in subsequence))