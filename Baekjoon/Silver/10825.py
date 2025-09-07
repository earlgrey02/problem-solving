import sys

input = sys.stdin.readline

n = int(input())
scores = sorted((tuple(input().split()) for _ in range(n)), key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

print(*map(lambda x: x[0], scores), sep = '\n')