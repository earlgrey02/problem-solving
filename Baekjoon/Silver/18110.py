import sys
from math import floor
from statistics import mean

input = sys.stdin.readline

n = int(input())

ratings = sorted(int(input()) for _ in range(n))
border = floor(n * 0.15 + 0.5)

print(floor(mean(ratings[border:n - border]) + 0.5) if n > 0 else 0)