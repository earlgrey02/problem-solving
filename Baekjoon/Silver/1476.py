import sys
from functools import reduce

input = sys.stdin.readline

e, s, m = map(int, input().split())
today = [1, 1, 1]
boundaries = (15, 28, 19)
year = 1

while today != [e, s, m]:
    for i in range(3):
        if today[i] < boundaries[i]:
            today[i] += 1
        else:
            today[i] = 1

    year += 1

print(year)