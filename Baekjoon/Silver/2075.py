import sys
from heapq import heapify, heappop, heappush

input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    for i in map(int, input().split()):
        if len(heap) < n:
            heappush(heap, i)
        elif heap[0] < i:
            heappush(heap, i)
            heappop(heap)

print(heap[0])