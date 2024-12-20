import sys

input = sys.stdin.readline

n, b = map(int, input().split())
numbers = (*map(str, range(0, 10)), *map(chr, range(ord('A'), ord('Z') + 1)))
remains = []

while n:
    remains.append(n % b)
    n //= b

print(*(numbers[i] for i in reversed(remains)), sep = '')