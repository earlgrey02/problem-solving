import sys

input = sys.stdin.readline

n = int(input())

print((n - 2) * (n - 1) * n // 6, 3, sep = '\n')