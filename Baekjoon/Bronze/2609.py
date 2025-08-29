import sys
from math import gcd, lcm

input = sys.stdin.readline

a, b = map(int, input().split())

print(gcd(a, b), lcm(a, b), sep = '\n')