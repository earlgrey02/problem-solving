import sys

input = sys.stdin.readline

n, k = map(int, input().split())
number = list(map(int, input().strip()))
stack = []

for digit in number:
    while stack and stack[-1] < digit and k > 0:
        stack.pop()
        k -= 1

    stack.append(digit)

print(*stack[:-k if k > 0 else None], sep = '')