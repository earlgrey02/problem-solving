from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
queue = deque()

for _ in range(n):
    commands = list(input().split())
    operation = commands[0]

    if operation == "push":
        queue.append(int(commands[1]))
    elif operation == "pop":
        print(queue.popleft() if queue else -1)
    elif operation == "size":
        print(len(queue))
    elif operation == "empty":
        print(int(not queue))
    elif operation == "front":
        print(queue[0] if queue else -1)
    elif operation == "back":
        print(queue[-1] if queue else -1)