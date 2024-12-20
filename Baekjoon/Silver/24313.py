import sys

input = sys.stdin.readline

a1, a0 = map(int, input().split())
c = int(input())
n = int(input())

print(int(a1 * n + a0 <= c * n and a1 <= c))