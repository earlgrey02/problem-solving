import sys

input = sys.stdin.readline

n = int(input())
towers = list(map(int, input().split()))
stack = []
result = [0 for _ in range(n)]

for i in range(n - 1, -1, -1):
    while stack and towers[stack[-1]] < towers[i]:
        result[stack.pop()] = i + 1

    stack.append(i)

print(*result)