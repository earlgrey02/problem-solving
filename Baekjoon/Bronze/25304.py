import sys

input = sys.stdin.readline

x, n = (int(input()) for _ in range(2))
total = 0

for _ in range(n):
    a, b = map(int, input().split())
    total += a * b

if x == total:
    print("Yes")
else:
    print("No")