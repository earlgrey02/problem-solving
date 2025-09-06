import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

print(max(sum(abs(i - j) for i, j in zip(case, case[1:])) for case in permutations(numbers, n)))