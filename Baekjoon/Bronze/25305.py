import sys

input = sys.stdin.readline

_, k = map(int, input().split())
scores = map(int, input().split())

print(sorted(scores, reverse = True)[k - 1])