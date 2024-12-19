from statistics import mean
import sys

input = sys.stdin.readline

_ = input()
numbers = list(map(int, input().split()))

print(mean(map(lambda x: x / max(numbers) * 100, numbers)))