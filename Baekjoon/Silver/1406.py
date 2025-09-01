import sys
from collections import deque

input = sys.stdin.readline

string = input().strip()
m = int(input())
left, right = list(string), deque()

for _ in range(m):
    operator, *operand = input().split()

    if operator == 'L' and left:
        right.appendleft(left.pop())
    elif operator == 'D' and right:
        left.append(right.popleft())
    elif operator == 'B' and left:
        left.pop()
    elif operator == 'P':
        left.append(*operand)

print(*left, *right, sep = '')