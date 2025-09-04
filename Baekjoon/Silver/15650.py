import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())

print(*(' '.join(case) for case in combinations(map(str, range(1, n + 1)), m)), sep = '\n')