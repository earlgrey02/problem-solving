import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    r, s = input().split()

    print(*(i * int(r) for i in s), sep = "")