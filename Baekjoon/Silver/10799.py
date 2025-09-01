import sys

input = sys.stdin.readline

parentheses = input().strip()
stack = []
count = 0

for i, parenthesis in enumerate(parentheses):
    if parenthesis == '(':
        stack.append(parenthesis)
    else:
        stack.pop()
        count += len(stack) if parentheses[i - 1] == '(' else 1

print(count)