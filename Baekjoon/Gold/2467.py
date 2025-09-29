import sys
from math import inf

input = sys.stdin.readline

n = int(input())
solutions = sorted(map(int, input().split()))
left, right = 0, n - 1
neutral_solutions = (inf, inf)

while left < right:
    neutral_solutions = min(neutral_solutions, (solutions[left], solutions[right]), key = lambda x: abs(sum(x)))

    if solutions[left] + solutions[right] > 0:
        right -= 1
    else:
        left += 1

print(*neutral_solutions)