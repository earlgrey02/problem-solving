import sys
from bisect import bisect_right

input = sys.stdin.readline

n = int(input())
cranes = sorted(map(int, input().split()), reverse = True)
m = int(input())
boxes = sorted(map(int, input().split()))
time = 0

if boxes[-1] <= cranes[0]:
    while boxes:
        for crane in cranes:
            if (index := bisect_right(boxes, crane) - 1) >= 0:
                boxes.pop(index)

        time += 1
else:
    time = -1

print(time)