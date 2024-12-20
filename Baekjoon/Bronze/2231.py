import sys

input = sys.stdin.readline

n = int(input())
answer = 0

for i in range(n):
    if i + sum(map(int, str(i))) == n:
        answer = i
        break

print(answer)