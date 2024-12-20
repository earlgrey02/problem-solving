import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    c = int(input())
    coins = {25: 0, 10: 0, 5: 0, 1: 0}

    for coin in coins.keys():
        coins[coin] = c // coin
        c %= coin

    print(*coins.values())