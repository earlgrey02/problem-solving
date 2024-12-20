import sys

input = sys.stdin.readline

n = int(input())
answer = 0

while n:
    if "666" in str(answer := answer + 1):
        n -= 1

print(answer)