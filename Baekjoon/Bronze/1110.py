import sys

input = sys.stdin.readline

n = origin = int(input().strip())
count = 1

while origin != (n := (n % 10) * 10 + (n // 10 + n % 10) % 10):
    count += 1

print(count)