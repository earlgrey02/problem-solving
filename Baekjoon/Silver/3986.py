import sys

input = sys.stdin.readline

n = int(input())
words = [input().strip() for _ in range(n)]
count = 0

for word in words:
    stack = []

    for letter in word:
        if stack and stack[-1] == letter:
            stack.pop()
        else:
            stack.append(letter)

    if not stack:
        count += 1

print(count)