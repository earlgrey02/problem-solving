from math import inf
import sys

input = sys.stdin.readline

def dfs(depth: int, total: int):
    global maximum, minimum

    if depth == n:
        maximum, minimum = max(maximum, total), min(minimum, total)
    else:
        for i in range(4):
            if operators[i] > 0:
                operators[i] -= 1
                dfs(depth + 1, calculate[i](total, numbers[depth]))
                operators[i] += 1

n = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))
calculate = (lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: int(x / y))
maximum, minimum = -inf, inf

dfs(1, numbers[0])

print(maximum, minimum, sep = '\n')