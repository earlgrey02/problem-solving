import sys
from collections import Counter

input = sys.stdin.readline

def union(v1: int, v2: int):
    v1, v2 = find(v1), find(v2)

    if v1 != v2:
        if ranks[v1] == ranks[v2]:
            parents[v2] = v1
            ranks[v1] += 1
        elif ranks[v1] < ranks[v2]:
            parents[v1] = v2
        else:
            parents[v2] = v1

def find(v: int) -> int:
    if parents[v] != v:
        parents[v] = find(parents[v])

    return parents[v]

def counter_clockwise(v1: tuple[int, int], v2: tuple[int, int], v3: tuple[int, int]) -> int:
    return (v2[0] - v1[0]) * (v3[1] - v1[1]) - (v2[1] - v1[1]) * (v3[0] - v1[0])

def is_intersect(line1: tuple[tuple[int, int], tuple[int, int]], line2: tuple[tuple[int, int], tuple[int, int]]) -> bool:
    ccw1 = counter_clockwise(line1[0], line1[1], line2[0]) * counter_clockwise(line1[0], line1[1], line2[1])
    ccw2 = counter_clockwise(line2[0], line2[1], line1[0]) * counter_clockwise(line2[0], line2[1], line1[1])

    if ccw1 == 0 and ccw2 == 0:
        return max(line1[0][0], line1[1][0]) >= min(line2[0][0], line2[1][0]) and max(line2[0][0], line2[1][0]) >= min(line1[0][0], line1[1][0]) and max(line1[0][1], line1[1][1]) >= min(line2[0][1], line2[1][1]) and max(line2[0][1], line2[1][1]) >= min(line1[0][1], line1[1][1])
    else:
        return ccw1 <= 0 and ccw2 <= 0

n = int(input())
lines = [tuple(tuple(line[i:i + 2]) for i in range(0, 4, 2)) for line in (list(map(int, input().split())) for _ in range(n))]
parents = [i for i in range(n)]
ranks = [0 for _ in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        if is_intersect(lines[i], lines[j]):
            union(i, j)

print(len(counter := Counter(find(i) for i in range(n))))
print(max(counter.values()))