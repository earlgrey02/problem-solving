import sys

input = sys.stdin.readline

n = input().strip()
count = (int(n) - (10 ** (len(n) - 1)) + 1) * len(n)
mod = 1234567

for i in range(len(n) - 1):
    count += (9 * (10 ** i) * (i + 1)) % mod

print(count % mod)