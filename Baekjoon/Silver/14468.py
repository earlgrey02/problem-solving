import sys

input = sys.stdin.readline

histories = list(input().strip())
stack = []
count = 0

for i in histories:
    if i in stack:
        count += len(stack) - (index := stack.index(i)) - 1
        stack.pop(index)
    else:
        stack.append(i)

print(count)