import sys

input = sys.stdin.readline

k, n = map(int, input().split())
cables = [int(input()) for _ in range(k)]
start, end = 1, max(cables)

while start <= end:
    mid = (start + end) // 2
    count = sum(cable // mid for cable in cables if cable >= mid)

    if count >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)