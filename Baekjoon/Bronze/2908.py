import sys

input = sys.stdin.readline

numbers = input().split()

print(max(map(lambda x: int(x[::-1]), numbers)))