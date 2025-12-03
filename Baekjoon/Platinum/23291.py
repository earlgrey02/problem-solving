import sys

input = sys.stdin.readline

def stack_up(tanks: list[list[int]], order: int):
    if order == 0:
        result = [tanks.pop(0)]

        while len(tanks) >= len(result[0]):
            result = [tanks.pop(0) + i for i in map(list, zip(*result[::-1]))]

        tanks[:0] = result
    elif order == 1:
        for i in range(2):
            mid = n >> (i + 1)
            half = [tanks.pop(0)[::-1] for _ in range(mid)][::-1]

            for j in range(mid):
                tanks[j].extend(half[j])

def adjust_population(tanks: list[list[int]]):
    diffs = [[0 for _ in range(len(tanks[i]))] for i in range(len(tanks))]

    for i in range(len(tanks)):
        for j in range(len(tanks[i])):
            for k in range(4):
                next_v = (i + dy[k], j + dx[k])

                if 0 <= next_v[0] < len(tanks) and 0 <= next_v[1] < len(tanks[next_v[0]]) and (diff := (tanks[i][j] - tanks[next_v[0]][next_v[1]]) // 5) > 0:
                    diffs[i][j] -= diff
                    diffs[next_v[0]][next_v[1]] += diff

    for i in range(len(tanks)):
        for j in range(len(tanks[i])):
            tanks[i][j] += diffs[i][j]

n, k = map(int, input().split())
tanks = [[i] for i in map(int, input().split())]
count = 0
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

while max(flatten_tanks := [i for tank in tanks for i in tank]) - (min_fish := min(flatten_tanks)) > k:
    for tank in tanks:
        if tank[0] == min_fish:
            tank[0] += 1

    for i in range(2):
        stack_up(tanks, i)
        adjust_population(tanks)
        tanks = [[i] for tank in tanks for i in tank]

    count += 1

print(count)