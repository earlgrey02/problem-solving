from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
balloons = deque(enumerate(map(int, input().split())))
sequence = []

while balloons:
    index, number = balloons.popleft()
    sequence.append(index + 1)

    balloons.rotate(-(number - 1) if number > 0 else -number)

print(*sequence)