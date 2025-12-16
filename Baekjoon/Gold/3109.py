import sys

input = sys.stdin.readline

def dfs(v: tuple[int, int]) -> bool:
    visited[v[0]][v[1]] = True

    for i in range(3):
        next_v = (v[0] + dy[i], v[1] + dx[i])

        if 0 <= next_v[0] < r and 0 <= next_v[1] < c and matrix[next_v[0]][next_v[1]] == '.' and not visited[next_v[0]][next_v[1]] and (next_v[1] == c - 1 or dfs(next_v)):
            return True

    return False

r, c = map(int, input().split())
matrix = [list(input().strip()) for _ in range(r)]
visited = [[False for _ in range(c)] for _ in range(r)]
dy = (-1, 0, 1)
dx = (1, 1, 1)

print(sum(1 for i in range(r) if dfs((i, 0))))