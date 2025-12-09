import sys
from collections import deque

input = sys.stdin.readline

n, l = map(int, input().split())
numbers = list(map(int, input().split()))
queue = deque()

for i in range(n):
    while queue and queue[-1][0] >= numbers[i]:
        queue.pop()

    queue.append((numbers[i], i))

    if queue[0][1] <= i - l:
        queue.popleft()

    print(queue[0][0], end = ' ')