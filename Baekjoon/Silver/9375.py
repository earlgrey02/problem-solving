import sys
from collections import Counter
from math import prod

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    counter = Counter(input().split()[1] for _ in range(n))

    print(prod(map(lambda x: x + 1, counter.values())) - 1)