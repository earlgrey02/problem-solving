import sys
from collections import deque

input = sys.stdin.readline

s, t = (list(input().strip()) for _ in range(2))

while s != t and t:
    if t.pop() == 'B':
        t.reverse()

print(int(s == t))