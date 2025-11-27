import sys
from math import ceil

input = sys.stdin.readline

n, l = map(int, input().split())
pools = sorted(tuple(map(int, input().split())) for _ in range(n))
end = 0
count = 0

for pool in pools:
    if pool[0] < end:
        pool = (end, pool[1])

    length = pool[1] - pool[0]
    count += ceil(length / l)
    end = pool[0] + l * ceil(length / l)

print(count)