import sys

input = sys.stdin.readline

n, m = map(int, input().split())
baskets = [0 for _ in range(n + 1)]

for _ in range(m):
    i, j, k = map(int, input().split())

    baskets[i:j + 1] = [k for _ in range(j - i + 1)]

print(*baskets[1:])
