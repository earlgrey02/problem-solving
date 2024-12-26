from itertools import combinations_with_replacement
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

print(*(' '.join(map(str, case)) for case in sorted(combinations_with_replacement(range(1, n + 1), m))), sep = '\n')