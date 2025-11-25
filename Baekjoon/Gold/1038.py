import sys
from collections import deque

input = sys.stdin.readline

def bfs(numbers: list[int]) -> int:
    queue = deque(numbers)
    count = -1

    while queue:
        v = queue.popleft()
        count += 1

        if count == n:
            return v

        for i in range(int(str(v)[-1])):
            queue.append(v * 10 + i)

    return -1

n = int(input())

print(bfs(list(range(10))))