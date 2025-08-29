import sys

input = sys.stdin.readline

n = int(input())
budgets = list(map(int, input().split()))
m = int(input())
start, end = 1, max(budgets)

while start <= end:
    mid = (start + end) // 2
    cost = sum(min(mid, budget) for budget in budgets)

    if cost <= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)