import sys

input = sys.stdin.readline

n = int(input())
max_dp = min_dp = tuple(map(int, input().split()))

for i in range(n - 1):
    a, b, c = map(int, input().split())

    max_dp = (a + max(max_dp[:2]), b + max(max_dp[:]), c + max(max_dp[1:]))
    min_dp = (a + min(min_dp[:2]), b + min(min_dp[:]), c + min(min_dp[1:]))

print(max(max_dp), min(min_dp))