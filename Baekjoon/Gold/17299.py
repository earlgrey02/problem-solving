import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
sequence = list(map(int, input().split()))
counter = Counter(sequence)
ngf = [-1 for _ in range(n)]
stack = []

for i in range(n):
    while stack and counter[sequence[stack[-1]]] < counter[sequence[i]]:
        ngf[stack.pop()] = sequence[i]

    stack.append(i)

print(*ngf)