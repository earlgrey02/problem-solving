import sys

input = sys.stdin.readline

_ = input()
numbers = list(map(int, input().split()))

print(min(numbers), max(numbers))