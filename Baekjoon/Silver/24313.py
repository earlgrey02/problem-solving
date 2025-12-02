import sys

input = sys.stdin.readline

a1, a0 = map(int, input().split())
c, n = (int(input()) for _ in range(2))

print(int(a1 * n + a0 <= c * n and a1 <= c))