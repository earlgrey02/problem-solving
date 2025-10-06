import sys
from itertools import accumulate
from math import inf

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    files = list(map(int, input().split()))
    dp = [[inf if i != j else 0 for j in range(n)] for i in range(n)]
    prefix_sum = [0] + list(accumulate(files))

    for i in range(1, n):
        for j in range(n - i):
            for k in range(j, j + i):
                dp[j][j + i] = min(dp[j][j + i], dp[j][k] + dp[k + 1][j + i] + prefix_sum[j + i + 1] - prefix_sum[j])

    print(dp[0][-1])