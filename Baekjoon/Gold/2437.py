import sys

input = sys.stdin.readline

n = int(input())
weights = sorted(map(int, input().split()))
summation = 0

for weight in weights:
    if summation + 1 < weight:
        break

    summation += weight

print(summation + 1)