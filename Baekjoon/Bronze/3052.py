import sys

input = sys.stdin.readline

print(len({int(input()) % 42 for _ in range(10)}))