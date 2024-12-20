import sys

input = sys.stdin.readline

sides = tuple(map(int, input().split()))
perimeter = sum(sides)

print(perimeter if perimeter > 2 * max(sides) else 2 * perimeter - 2 * max(sides) - 1)