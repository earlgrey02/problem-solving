import sys

input = sys.stdin.readline

n = int(input())
a, b = (sorted(map(int, input().split()), reverse = bool(i)) for i in range(2))

print(sum(i * j for i, j in zip(a, b)))