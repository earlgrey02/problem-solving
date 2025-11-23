import sys
from math import inf

input = sys.stdin.readline

n = int(input())
solutions = sorted(map(int, input().split()))
neutral_solutions = (inf, inf, inf)

for i in range(n - 2):
    left, right = i + 1, n - 1

    while left < right:
        neutral_solutions = min(neutral_solutions, (solutions[i], solutions[left], solutions[right]), key = lambda x: abs(sum(x)))

        if solutions[i] + solutions[left] + solutions[right] > 0:
            right -= 1
        else:
            left += 1

print(*neutral_solutions)