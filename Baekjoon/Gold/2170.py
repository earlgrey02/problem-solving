import sys

input = sys.stdin.readline

n = int(input())
lines = sorted(tuple(map(int, input().split())) for _ in range(n))
start, end = lines[0]
length = 0

for line in lines[1:]:
    if line[0] > end:
        length += end - start
        start, end = line
    elif line[1] > end:
        end = line[1]

print(length + (end - start))