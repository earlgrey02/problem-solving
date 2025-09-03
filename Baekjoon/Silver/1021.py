import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
queue = deque(i for i in range(1, n + 1))
count = 0

for i in map(int, input().split()):
    while queue[0] != i:
        count += 1

        if queue.index(i) <= len(queue) // 2:
            queue.append(queue.popleft())
        else:
            queue.appendleft(queue.pop())

    queue.popleft()

print(count)