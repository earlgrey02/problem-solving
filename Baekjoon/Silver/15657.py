import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline

n, m = map(int, input().split())
numbers = sorted(map(int, input().split()))

print(*(' '.join(case) for case in combinations_with_replacement(map(str, numbers), m)), sep = '\n')