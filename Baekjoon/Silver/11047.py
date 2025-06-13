import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)][::-1]
count = 0

for coin in coins:
    count += k // coin
    k %= coin

print(count)