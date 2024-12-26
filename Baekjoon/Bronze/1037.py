import sys

input = sys.stdin.readline

_ = int(input())
numbers = list(map(int, input().split()))

print(max(numbers) * min(numbers))