from math import floor, sqrt
import sys

input = sys.stdin.readline

x = int(input())
line = floor((1 + sqrt(8 * x - 7)) / 2)
index = int((line * (line - 1)) / 2) + 1
fraction = ((x - index) + 1, line - (x - index))

print(*(fraction if line % 2 == 0 else reversed(fraction)), sep = '/')