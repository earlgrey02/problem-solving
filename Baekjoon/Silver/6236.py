import sys

input = sys.stdin.readline

n, m = map(int, input().split())
costs = [int(input()) for _ in range(n)]
start, end = max(costs), sum(costs)

while start <= end:
    mid = (start + end) // 2
    count = remains = 0

    for cost in costs:
        if remains < cost:
            count += 1
            remains = mid

        remains -= cost

    if count > m:
        start = mid + 1
    else:
        end = mid - 1

print(start)