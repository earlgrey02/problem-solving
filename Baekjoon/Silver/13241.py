from math import lcm
import sys

input = sys.stdin.readline

print(lcm(*map(int, input().split())), sep = '\n')