import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
belt = deque([durability, False] for durability in map(int, input().split()))
count = 0

while k > 0:
    belt.rotate()
    belt[n - 1][1] = False

    for i in range(n - 2, -1, -1):
        if belt[i][1] and belt[i + 1][0] > 0 and not belt[i + 1][1]:
            belt[i][1], belt[i + 1][1] = belt[i + 1][1], belt[i][1]
            belt[i + 1][0] -= 1

            if belt[i + 1][0] == 0:
                k -= 1

    belt[n - 1][1] = False

    if belt[0][0] > 0:
        belt[0][0] -= 1
        belt[0][1] = True

        if belt[0][0] == 0:
            k -= 1

    count += 1

print(count)