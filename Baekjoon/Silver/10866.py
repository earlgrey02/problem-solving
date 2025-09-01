import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
queue = deque()

for _ in range(n):
    operator, *operand = input().split()

    if operator == "push_front":
        queue.appendleft(*operand)
    elif operator == "push_back":
        queue.append(*operand)
    elif operator == "pop_front":
        print(queue.popleft() if queue else -1)
    elif operator == "pop_back":
        print(queue.pop() if queue else -1)
    elif operator == "size":
        print(len(queue))
    elif operator == "empty":
        print(int(not queue))
    elif operator == "front":
        print(queue[0] if queue else -1)
    elif operator == "back":
        print(queue[-1] if queue else -1)