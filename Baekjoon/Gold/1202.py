import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n, k = map(int, input().split())
jewels = sorted(tuple(map(int, input().split())) for _ in range(n))
bags = sorted(int(input()) for _ in range(k))
heap = []
value = 0
i = 0

for bag in bags:
    while i < n and jewels[i][0] <= bag:
        heappush(heap, -jewels[i][1])
        i += 1

    if heap:
        value -= heappop(heap)

print(value)