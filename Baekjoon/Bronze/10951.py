import sys

input = sys.stdin.readline

while numbers := input().split():
    print(sum(map(int, numbers)))