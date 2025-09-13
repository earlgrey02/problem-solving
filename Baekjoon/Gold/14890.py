import sys

input = sys.stdin.readline

def check(road: list[int]) -> bool:
    is_slopes = [False for _ in range(n)]
    i = 0

    while i < n - 1:
        if abs(road[i] - road[i + 1]) > 1:
            return False
        elif road[i] < road[i + 1]:
            for j in range(i, i - l, -1):
                if j >= 0 and road[j] == road[i] and not is_slopes[j]:
                    is_slopes[j] = True
                else:
                    return False
        elif road[i] > road[i + 1]:
            for j in range(i + 1, i + l + 1):
                if j < n and road[j] == road[i + 1] and not is_slopes[j]:
                    is_slopes[j] = True
                else:
                    return False

        i += 1

    return True

n, l = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

print(sum(check(row) for row in matrix) + sum(check(list(col)) for col in zip(*matrix)))