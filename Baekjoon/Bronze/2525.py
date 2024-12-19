import sys

input = sys.stdin.readline

a, b = map(int, input().split())
c = int(input())
total = (a * 60 + b) + c
a = total // 60 % 24
b = total % 60

print(a, b)