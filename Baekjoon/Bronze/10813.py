import sys

input = sys.stdin.readline

n, m = map(int, input().split())
numbers = [i for i in range(n + 1)]

for _ in range(m):
    i, j = map(int, input().split())

    numbers[i], numbers[j] = numbers[j], numbers[i]

print(*numbers[1:])