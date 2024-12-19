import sys

input = sys.stdin.readline

n, m = map(int, input().split())
numbers = [i for i in range(n + 1)]

for _ in range(m):
    i, j = map(int, input().split())

    numbers[i:j + 1] = numbers[j:i - 1:-1]

print(*numbers[1:])