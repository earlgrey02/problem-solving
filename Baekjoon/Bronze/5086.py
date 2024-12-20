import sys

input = sys.stdin.readline

while (numbers := tuple(map(int, input().split()))) != (0, 0):
    a, b = numbers

    if a % b == 0:
        print("multiple")
    elif b % a == 0:
        print("factor")
    else:
        print("neither")