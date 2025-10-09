import sys
from re import compile

input = sys.stdin.readline

expression = compile("(100+1+|01)+")

print("SUBMARINE" if expression.fullmatch(input().strip()) else "NOISE")