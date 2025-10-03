import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())
times = sorted(tuple(map(int, input().split())) for _ in range(n))
rooms = [times[0][1]]

for time in times[1:]:
    if rooms[0] <= time[0]:
        heappop(rooms)

    heappush(rooms, time[1])

print(len(rooms))