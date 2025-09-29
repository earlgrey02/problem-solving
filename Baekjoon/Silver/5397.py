import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    commands = input().strip()
    left, right = [], []

    for command in commands:
        if command.isalnum():
            left.append(command)
        elif command == '<' and left:
            right.append(left.pop())
        elif command == '>' and right:
            left.append(right.pop())
        elif command == '-' and left:
            left.pop()

    print(*left, *right[::-1], sep = '')