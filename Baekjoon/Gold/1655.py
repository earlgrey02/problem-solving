import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())
left, right = [], []

for i in (int(input()) for _ in range(n)):
    if len(left) == len(right):
        heappush(left, -i)
    else:
        heappush(right, i)

    if left and right and -left[0] > right[0]:
        left_temp = -heappop(left)
        right_temp = heappop(right)
        heappush(left, -right_temp)
        heappush(right, left_temp)

    print(-left[0])