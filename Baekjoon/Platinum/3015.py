import sys

input = sys.stdin.readline

n = int(input())
heights = [int(input()) for _ in range(n)]
stack = []
count = 0

for height in heights:
    if not stack or stack[-1][0] > height:
        stack.append([height, 1])
    elif stack[-1][0] < height:
        while stack and stack[-1][0] < height:
            count += stack.pop()[1]

        if stack and stack[-1][0] == height:
            count += stack[-1][1]
            stack[-1][1] += 1
        else:
            stack.append([height, 1])
    else:
        count += stack[-1][1]
        stack[-1][1] += 1

    if len(stack) > 1:
        count += 1

print(count)