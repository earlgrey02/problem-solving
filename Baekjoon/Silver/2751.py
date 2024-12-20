import sys

input = sys.stdin.readline

n = int(input())

print(*sorted(int(input()) for _ in range(n)), sep = '\n')