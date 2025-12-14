import sys
from math import inf

input = sys.stdin.readline

n, k = map(int, input().split())
orders = list(map(int, input().split()))
plugs = set()
count = 0

for i in range(k):
    if orders[i] in plugs:
        continue

    if len(plugs) == n:
        plugs.remove(max(plugs, key = lambda x: orders.index(x, i + 1) if x in orders[i + 1:] else inf))
        count += 1

    plugs.add(orders[i])

print(count)