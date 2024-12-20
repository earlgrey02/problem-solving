import sys

input = sys.stdin.readline

numbers = map(int, input().strip())

print(*sorted(numbers, reverse = True), sep = '')