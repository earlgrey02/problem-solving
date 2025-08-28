import sys

input = sys.stdin.readline

t = int(input())
times = [300, 60, 10]
count = [0, 0, 0]

for i in range(3):
    count[i] += t // times[i]
    t %= times[i]

print(*count if t == 0 else [-1])