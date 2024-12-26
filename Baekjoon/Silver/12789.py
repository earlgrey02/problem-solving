import sys

input = sys.stdin.readline

n = int(input())
stack = []
current = 1

for i in map(int, input().split()):
    stack.append(i)

    while stack and stack[-1] == current:
        stack.pop()
        current += 1

print("Sad" if stack else "Nice")