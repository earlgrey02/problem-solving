import sys
from re import compile

input = sys.stdin.readline

t = int(input())
expression = compile("(100+1+|01)+")

for _ in range(t):
    print("YES" if expression.fullmatch(input().strip()) else "NO")