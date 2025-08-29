import sys

input = sys.stdin.readline

a, b, c = (int(input()) for _ in range(3))
result = list(map(int, str(a * b * c)))

print(*(result.count(i) for i in range(10)), sep = '\n')