import sys

input = sys.stdin.readline

while (sides := tuple(map(int, input().split()))) != (0, 0, 0):
    if sum(sides) > 2 * max(sides):
        count = len(set(sides))

        if count == 1:
            print("Equilateral")
        elif count == 2:
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Invalid")
