import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
numbers = sorted(map(int, input().split()))

print(*(' '.join(case) for case in dict.fromkeys(combinations(map(str, numbers), m))), sep = '\n')