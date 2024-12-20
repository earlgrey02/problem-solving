from math import ceil, sqrt
import sys

input = sys.stdin.readline

print(ceil((1 + sqrt(1 + 8 * ((int(input()) - 1) / 6))) / 2))