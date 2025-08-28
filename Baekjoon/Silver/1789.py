import sys
from math import isqrt

input = sys.stdin.readline

s = int(input())

print((isqrt(1 + s * 8) - 1) // 2)