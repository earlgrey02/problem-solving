import sys

input = sys.stdin.readline

_, x = map(int, input().split())
numbers = list(map(int, input().split()))

print(*filter(lambda y: y < x, numbers))