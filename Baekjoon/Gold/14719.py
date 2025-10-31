import sys

input = sys.stdin.readline

h, w = map(int, input().split())
blocks = list(map(int, input().split()))
amount = 0

for i in range(1, w - 1):
    amount += max(0, min(max(blocks[:i]), max(blocks[i + 1:])) - blocks[i])

print(amount)