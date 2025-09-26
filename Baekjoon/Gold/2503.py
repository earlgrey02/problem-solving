import sys

input = sys.stdin.readline

parentheses = input().strip()
stack = []
summation = 0
temp = 1

for i in range(len(parentheses)):
    if parentheses[i] == '(':
        stack.append(parentheses[i])
        temp *= 2
    elif parentheses[i] == '[':
        stack.append(parentheses[i])
        temp *= 3
    elif parentheses[i] == ')':
        if stack and stack.pop() == '(':
            if parentheses[i - 1] == '(':
                summation += temp

            temp //= 2
        else:
            summation = 0
            break
    elif parentheses[i] == ']':
        if stack and stack.pop() == '[':
            if parentheses[i - 1] == '[':
                summation += temp

            temp //= 3
        else:
            summation = 0
            break

print(summation if not stack else 0)