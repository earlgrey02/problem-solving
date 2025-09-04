import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline

n, m = map(int, input().split())

print(*(' '.join(case) for case in combinations_with_replacement(map(str, range(1, n + 1)), m)), sep = '\n')