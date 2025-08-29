import sys

input = sys.stdin.readline

n, k = (int(input()) for _ in range(2))
start, end = 1, k

while start <= end:
    mid = (start + end) // 2
    count = sum(min(n, mid // i) for i in range(1, n + 1))

    if count < k:
        start = mid + 1
    else:
        end = mid - 1

print(start)