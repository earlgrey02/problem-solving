import sys
from math import copysign

input = sys.stdin.readline

def counter_clockwise(v1: tuple[int, int], v2: tuple[int, int], v3: tuple[int, int]) -> int:
    return (v2[0] - v1[0]) * (v3[1] - v1[1]) - (v2[1] - v1[1]) * (v3[0] - v1[0])

points = [tuple(map(int, input().split())) for _ in range(3)]

print(int(copysign(1, ccw)) if (ccw := counter_clockwise(*points)) != 0 else 0)