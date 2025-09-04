import sys
from itertools import permutations

input = sys.stdin.readline

n, m = map(int, input().split())

print(*(' '.join(case) for case in permutations(map(str, range(1, n + 1)), m)), sep = '\n')