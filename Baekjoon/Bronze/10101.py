import sys

input = sys.stdin.readline

angles = [int(input()) for _ in range(3)]

if sum(angles) == 180:
    count = len(set(angles))

    if count == 1:
        print("Equilateral")
    elif count == 2:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")