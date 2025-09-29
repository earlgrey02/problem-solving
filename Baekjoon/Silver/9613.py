import sys
from itertools import combinations
from math import gcd

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    numbers = list(map(int, input().split()))[1:]

    print(sum(gcd(*case) for case in combinations(numbers, 2)))