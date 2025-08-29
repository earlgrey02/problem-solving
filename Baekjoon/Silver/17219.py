import sys

input = sys.stdin.readline

n, m = map(int, input().split())
passwords = dict(input().split() for _ in range(n))

print(*(passwords[input().strip()] for _ in range(m)), sep = '\n')