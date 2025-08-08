import sys
from collections import deque

input = sys.stdin.readline

cogwheels = [list(map(int, input().strip())) for _ in range(4)]
k = int(input())
rotations = [tuple(map(int, input().split())) for _ in range(k)]

for rotation in ((i - 1, j) for i, j in rotations):
    rotated = [False for _ in range(4)]
    queue = deque([rotation])

    while queue:
        index, d = queue.popleft()
        rotated[index] = True

        if index > 0 and cogwheels[index][6] != cogwheels[index - 1][2] and not rotated[index - 1]:
            queue.append((index - 1, -d))
        if index < 3 and cogwheels[index][2] != cogwheels[index + 1][6] and not rotated[index + 1]:
            queue.append((index + 1, -d))

        if d == 1:
            cogwheels[index] = [cogwheels[index][-1], *cogwheels[index][:-1]]
        else:
            cogwheels[index] = [*cogwheels[index][1:], cogwheels[index][0]]

print(sum(cogwheels[i][0] * (2 ** i) for i in range(4)))