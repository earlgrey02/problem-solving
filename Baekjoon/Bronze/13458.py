import sys
from math import ceil

input = sys.stdin.readline

n = int(input())
rooms = list(map(int, input().split()))
b, c = map(int, input().split())

print(sum(max(ceil((room - b) / c), 0) + 1 for room in rooms))