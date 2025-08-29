import sys

input = sys.stdin.readline

while (sides := tuple(map(int, input().split()))) != (0, 0, 0):
    a, b, c = sorted(sides)

    print("right "if a ** 2 + b ** 2 == c ** 2 else "wrong")