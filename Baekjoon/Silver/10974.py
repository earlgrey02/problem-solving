import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())

print(*(' '.join(case) for case in permutations(map(str, range(1, n + 1)), n)), sep = '\n')