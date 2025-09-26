import sys

input = sys.stdin.readline

_ = input()

print(*sorted(i for _ in range(2) for i in map(int, input().split())))