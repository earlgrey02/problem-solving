import sys

input = sys.stdin.readline

h, m = map(int, input().split())
total = (h * 60 + m) - 45
h = total // 60 % 24
m = total % 60

print(h, m)
