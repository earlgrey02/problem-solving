import sys
from bisect import bisect_left

input = sys.stdin.readline

while True:
    try:
        n = int(input())
        prices = list(map(int, input().split()))
        dp = [prices[0]]

        for i in range(n):
            if dp[-1] < prices[i]:
                dp.append(prices[i])
            else:
                dp[bisect_left(dp, prices[i])] = prices[i]

        print(len(dp))
    except (EOFError, ValueError):
        break