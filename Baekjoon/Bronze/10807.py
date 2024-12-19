import sys

input = sys.stdin.readline

_ = input()
numbers = list(map(int, input().split()))
v = int(input())

print(numbers.count(v))