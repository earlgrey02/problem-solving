import sys
from math import comb

input = sys.stdin.readline

n, k = map(int, input().split())

print(comb(n, k) % 10007)