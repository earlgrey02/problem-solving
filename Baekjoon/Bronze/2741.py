import sys

input = sys.stdin.readline

n = int(input())

print(*range(1, n + 1), sep = '\n')