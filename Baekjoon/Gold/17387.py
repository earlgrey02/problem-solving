import sys

input = sys.stdin.readline

def counter_clockwise(v1: tuple[int, int], v2: tuple[int, int], v3: tuple[int, int]) -> int:
    return (v2[0] - v1[0]) * (v3[1] - v1[1]) - (v2[1] - v1[1]) * (v3[0] - v1[0])

def is_intersect(line1: tuple[tuple[int, int], tuple[int, int]], line2: tuple[tuple[int, int], tuple[int, int]]) -> bool:
    ccw1 = counter_clockwise(line1[0], line1[1], line2[0]) * counter_clockwise(line1[0], line1[1], line2[1])
    ccw2 = counter_clockwise(line2[0], line2[1], line1[0]) * counter_clockwise(line2[0], line2[1], line1[1])

    if ccw1 == 0 and ccw2 == 0:
        return all((
            max(line1[0][0], line1[1][0]) >= min(line2[0][0], line2[1][0]),
            max(line2[0][0], line2[1][0]) >= min(line1[0][0], line1[1][0]),
            max(line1[0][1], line1[1][1]) >= min(line2[0][1], line2[1][1]),
            max(line2[0][1], line2[1][1]) >= min(line1[0][1], line1[1][1]),
        ))
    else:
        return ccw1 <= 0 and ccw2 <= 0

lines = [tuple(tuple(line[i:i + 2]) for i in range(0, 4, 2)) for line in (list(map(int, input().split())) for _ in range(2))]

print(int(is_intersect(*lines)))