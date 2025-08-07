import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
k = int(input())
apples = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(k)]
l = int(input())
actions = [tuple(map(lambda x: int(x) if x.isdigit() else x, input().split())) for _ in range(l)]
snake = deque([(0, 0)])
d = 0
answer = 0
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

while True:
    answer += 1
    head = snake[-1]
    next_head = (head[0] + dy[d], head[1] + dx[d])

    if 0 <= next_head[0] < n and 0 <= next_head[1] < n and next_head not in snake:
        if next_head in apples:
            apples.remove(next_head)
            snake.append(next_head)
        else:
            snake.popleft()
            snake.append(next_head)
    else:
        break

    if action := next((action for action in actions if action[0] == answer), None):
        d = (d + (1 if action[1] == 'D' else 3)) % 4

print(answer)