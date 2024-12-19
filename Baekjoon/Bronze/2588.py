import sys

input = sys.stdin.readline

a, b = (int(input()) for _ in range(2))

print(*(a * int(i) for i in reversed(str(b))), sep = '\n')
print(a * b)