import sys
from itertools import permutations

input = sys.stdin.readline

n, m = map(int, input().split())
numbers = sorted(map(int, input().split()))

print(*(' '.join(case) for case in permutations(map(str, numbers), m)), sep = '\n')