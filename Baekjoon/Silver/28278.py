import sys

input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    numbers = list(map(int, input().split()))
    operator = numbers[0]

    if operator == 1:
        stack.append(numbers[1])
    elif operator == 2:
        print(stack.pop() if stack else -1)
    elif operator == 3:
        print(len(stack))
    elif operator == 4:
        print(int(not stack))
    else:
        print(stack[-1] if stack else -1)