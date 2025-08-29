import sys

input = sys.stdin.readline

n, m = map(int, input().split())
lectures = list(map(int, input().split()))
start, end = max(lectures), sum(lectures)

while start <= end:
    mid = (start + end) // 2
    count = 1
    size = 0

    for lecture in lectures:
        if size + lecture > mid:
            count += 1
            size = lecture
        else:
            size += lecture

    if count > m:
        start = mid + 1
    else:
        end = mid - 1

print(start)