import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    parentheses = list(input().strip())
    is_correct = True
    count = 0

    for i in parentheses:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1

        if count < 0:
            is_correct = False
            break

    if count > 0:
        is_correct = False

    print("YES" if is_correct else "NO")