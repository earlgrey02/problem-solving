import sys

input = sys.stdin.readline

n = int(input())
numbers = set(map(int, input().split()))
m = int(input())

print(*(int(i in numbers) for i in map(int, input().split())), sep = '\n')