from math import lcm
import sys

input = sys.stdin.readline

t = int(input())

print(*(lcm(*map(int, input().split())) for _ in range(t)), sep = '\n')