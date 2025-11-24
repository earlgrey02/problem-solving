import sys

input = sys.stdin.readline

n, b = input().split()
numbers = (*map(str, range(0, 10)), *map(chr, range(ord('A'), ord('Z') + 1)))

print(sum(numbers.index(digit) * (int(b) ** i) for i, digit in enumerate(reversed(n))))