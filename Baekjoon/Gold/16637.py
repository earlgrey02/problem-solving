import sys
from math import inf

input = sys.stdin.readline

def dfs(result: int, depth: int):
    global maximum

    if depth == n - 1:
        maximum = max(maximum, result)
    else:
        if depth < n - 2:
            dfs(eval(f"{result} {expression[depth + 1]} {expression[depth + 2]}"), depth + 2)
        if depth < n - 4:
            dfs(eval(f"{result} {expression[depth + 1]} {eval(expression[depth + 2:depth + 5])}"), depth + 4)

n = int(input())
expression = input().strip()
maximum = -inf

dfs(int(expression[0]), 0)

print(maximum)