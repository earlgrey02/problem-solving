from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
queuestack = deque([i for is_stack, i in zip(*(map(int, input().split()) for _ in range(2))) if not is_stack])
m = int(input())
queuestack.extendleft(map(int, input().split()))

print(*list(queuestack)[-1:-(m + 1):-1])