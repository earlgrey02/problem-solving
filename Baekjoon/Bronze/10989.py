import sys

input = sys.stdin.readline

n = int(input())
numbers = [0 for _ in range(10001)]

for _ in range(n):
    numbers[int(input())] += 1

for i in range(10001):
    if numbers[i] > 0:
        print(*(i for _ in range(numbers[i])), sep = '\n')