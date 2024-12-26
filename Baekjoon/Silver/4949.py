import sys

input = sys.stdin.readline

pair = {')': '(', ']': '['}

while (string := input().rstrip()) != '.':
    stack = []
    is_correct = True

    for i in string:
        if i in pair.values():
            stack.append(i)
        elif i in pair.keys():
            if stack and stack[-1] == pair[i]:
                stack.pop()
            else:
                is_correct = False
                break

    if stack:
        is_correct = False

    print("yes" if is_correct else "no")