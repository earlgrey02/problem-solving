import sys
from collections import Counter
from math import inf

input = sys.stdin.readline

n, m, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
counter = Counter(matrix[i][j] for i in range(n) for j in range(m))
answer = (inf, -inf)

for height in range(257):
    time = 0
    block = b

    for i, count in counter.items():
        diff = (i - height) * count
        block += diff
        time += abs(diff * 2 if diff > 0 else diff)

    if block >= 0 and time <= answer[0]:
        answer = (time, height)

print(*answer)