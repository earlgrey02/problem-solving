import sys

input = sys.stdin.readline

def check() -> int:
    matched_count = 0

    for i in range(1, n + 1):
        start = i

        for j in range(1, h + 1):
            start += adjacencies[j][start]

        if start == i:
            matched_count += 1

    return matched_count

def backtracking(v: tuple[int, int], depth: int = 0):
    global count

    if (n - (matched_count := check())) > (count - depth - 1) * 2:
        return
    elif matched_count == n:
        count = min(count, depth)
    elif depth < 3:
        for i in range(v[0], h + 1):
            for j in range(1, n):
                if adjacencies[i][j] == 0 and adjacencies[i][j + 1] == 0:
                    adjacencies[i][j] = 1
                    adjacencies[i][j + 1] = -1
                    backtracking((i, j + 2), depth + 1)
                    adjacencies[i][j] = 0
                    adjacencies[i][j + 1] = 0

n, m, h = map(int, input().split())
adjacencies = [[0 for _ in range(n + 1)] for _ in range(h + 1)]
count = 4

for _ in range(m):
    a, b = map(int, input().split())
    adjacencies[a][b] = 1
    adjacencies[a][b + 1] = -1

backtracking((1, 1))

print(count if count < 4 else -1)