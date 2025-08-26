import heapq
import sys

input = sys.stdin.readline

n = int(input())
heapq.heapify(cards := [int(input()) for _ in range(n)])
count = 0

while len(cards) > 1:
    heapq.heappush(cards, temp := sum(heapq.heappop(cards) for _ in range(2)))
    count += temp

print(count)