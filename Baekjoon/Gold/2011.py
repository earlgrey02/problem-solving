import sys

input = sys.stdin.readline

n = len(password := list(map(int, input().strip())))
dp = [0 for _ in range(n)]
dp[0] = 1
mod = int(1e6)

if n > 1:
    dp[1] = int(password[1] != 0) + int(10 <= password[0] * 10 + password[1] <= 26)

for i in range(2, n):
    if password[i] != 0:
        dp[i] += dp[i - 1]

    if 10 <= password[i - 1] * 10 + password[i] <= 26:
        dp[i] += dp[i - 2]

    dp[i] %= mod

print(dp[-1] if password[0] != 0 else 0)