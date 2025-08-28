import sys

input = sys.stdin.readline

n = int(input())
ropes = sorted((int(input()) for _ in range(n)), reverse = True)

print(max(ropes[i] * (i + 1) for i in range(n)))