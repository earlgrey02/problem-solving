import sys

input = sys.stdin.readline

n = int(input())
sequence = list(map(int, input().split()))
stack = []
nge = [-1 for _ in range(n)]

for i in range(n):
    while stack and sequence[stack[-1]] < sequence[i]:
        nge[stack.pop()] = sequence[i]

    stack.append(i)

print(*nge)