import sys

input = sys.stdin.readline

t = int(input())
numbers = [int(input()) for _ in range(t)]
n = max(numbers)
dp = [0 for _ in range(n + 1)]
mod = int(1e9) + 9

dp[1] = 1
if n >= 2:
    dp[2] = 2
if n >= 3:
    dp[3] = 4

for i in range(4, n + 1):
    dp[i] = sum(dp[i - 3:i]) % mod

print(*(dp[i] % mod for i in numbers), sep = '\n')