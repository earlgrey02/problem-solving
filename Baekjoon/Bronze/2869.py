from math import ceil
import sys

input = sys.stdin.readline

a, b, v = map(int, input().split())

print(ceil((v - b) / (a - b)))