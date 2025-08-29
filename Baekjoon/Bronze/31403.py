import sys

input = sys.stdin.readline

a, b, c = (int(input()) for _ in range(3))

print(a + b - c)
print(int(str(a) + str(b)) - c)