import sys

input = sys.stdin.readline

n = int(input())
positions = {}
count = 0

for _ in range(n):
    cow, position = map(int, input().split())

    if cow in positions and positions[cow] != position:
        count += 1

    positions[cow] = position

print(count)