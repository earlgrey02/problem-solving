import sys
from bisect import bisect_left

input = sys.stdin.readline

def union(v1: int, v2: int):
    v1, v2 = find(v1), find(v2)

    if v1 != v2:
        parents[v2] = v1

def find(v: int) -> int:
    if parents[v] != v:
        parents[v] = find(parents[v])

    return parents[v]

g, p = (int(input()) for _ in range(2))
parents = [i for i in range(g + 1)]
gates = [i for i in range(g + 1)]
count = 0

for airplane in (int(input()) for _ in range(p)):
    if (parent := find(airplane)) > 0:
        count += 1
        union(parent - 1, parent)
    else:
        break

print(count)