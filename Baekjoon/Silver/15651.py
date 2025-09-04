import sys
from itertools import product

input = sys.stdin.readline

n, m = map(int, input().split())

print(*(' '.join(case) for case in product(map(str, range(1, n + 1)), repeat = m)), sep = '\n')