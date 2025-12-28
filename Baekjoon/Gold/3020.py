import sys

input = sys.stdin.readline

n, h = map(int, input().split())
prefix_sum = [0 for _ in range(h + 2)]

for i in range(n):
    height = int(input())

    if i % 2 == 0:
        prefix_sum[1] += 1
        prefix_sum[height + 1] -= 1
    else:
        prefix_sum[h - height + 1] += 1
        prefix_sum[h + 1] -= 1

for i in range(1, h + 1):
    prefix_sum[i] += prefix_sum[i - 1]

print(minimum := min(prefix_sum[1:h + 1]), prefix_sum[1:h + 1].count(minimum))