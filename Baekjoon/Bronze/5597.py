import sys

input = sys.stdin.readline

numbers = {int(input()) for _ in range(28)}

print(*sorted(set(range(1, 31)) - numbers), sep = '\n')