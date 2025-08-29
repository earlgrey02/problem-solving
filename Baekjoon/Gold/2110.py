import sys

input = sys.stdin.readline

n, c = map(int, input().split())
houses = sorted(int(input()) for _ in range(n))
start, end = 1, houses[-1] - houses[0]

while start <= end:
    mid = (start + end) // 2
    current = houses[0]
    count = 1

    for house in houses[1:]:
        if house - current >= mid:
            count += 1
            current = house

    if count >= c:
        start = mid + 1
    else:
        end = mid - 1

print(end)