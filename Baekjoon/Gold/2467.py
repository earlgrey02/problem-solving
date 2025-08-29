import sys
from math import inf

input = sys.stdin.readline

n = int(input())
solutions = sorted(map(int, input().split()))
left, right = 0, n - 1
neutral_solutions = (inf, inf)

while left < right:
    value = solutions[left] + solutions[right]

    if abs(value) < abs(sum(neutral_solutions)):
        neutral_solutions = (solutions[left], solutions[right])

    if value > 0:
        right -= 1
    else:
        left += 1

print(*neutral_solutions)