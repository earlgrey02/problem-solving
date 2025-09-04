import sys
from itertools import product

input = sys.stdin.readline

n, m = map(int, input().split())
numbers = sorted(map(int, input().split()))

print(*(' '.join(case) for case in product(map(str, numbers), repeat = m)), sep = '\n')