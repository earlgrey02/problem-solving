import sys

input = sys.stdin.readline

n, m = map(int, input().split())
names = {input().strip() for _ in range(n)}.intersection(input().strip() for _ in range(m))

print(len(names), *sorted(names), sep = '\n')