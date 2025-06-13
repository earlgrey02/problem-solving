import sys

input = sys.stdin.readline

n = int(input())
times = sorted([tuple(map(int, input().split())) for _ in range(n)], key = lambda x: (x[1], x[0]))
end = times[0][1]
count = 1

for i in range(1, n):
    if times[i][0] >= end:
        end = times[i][1]
        count += 1

print(count)