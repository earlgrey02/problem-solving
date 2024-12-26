from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
queue = deque()

for _ in range(n):
    commands = list(map(int, input().split()))
    operation = commands[0]

    if operation == 1:
        queue.appendleft(commands[1])
    elif operation == 2:
        queue.append(commands[1])
    elif operation == 3:
        print(queue.popleft() if queue else -1)
    elif operation == 4:
        print(queue.pop() if queue else -1)
    elif operation == 5:
        print(len(queue))
    elif operation == 6:
        print(int(not queue))
    elif operation == 7:
        print(queue[0] if queue else -1)
    elif operation == 8:
        print(queue[-1] if queue else -1)