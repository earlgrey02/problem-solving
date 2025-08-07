import sys

input = sys.stdin.readline

def is_uncleaned_around(v: tuple[int, int]) -> bool:
    for i in range(4):
        next_v = (v[0] + dy[i], v[1] + dx[i])

        if 0 <= next_v[0] < n and 0 <= next_v[1] < m and matrix[next_v[0]][next_v[1]] == 0:
            return True

    return False

n, m = map(int, input().split())
r, c, d = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
v = (r, c)
answer = 0
dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)

while True:
    if matrix[v[0]][v[1]] == 0:
        matrix[v[0]][v[1]] = 2
        answer += 1

    if is_uncleaned_around(v):
        d = (d + 3) % 4
        next_v = (v[0] + dy[d], v[1] + dx[d])

        if 0 <= next_v[0] < n and 0 <= next_v[1] < m and matrix[next_v[0]][next_v[1]] == 0:
            v = next_v
    else:
        back_d = (d + 2) % 4
        next_v = (v[0] + dy[back_d], v[1] + dx[back_d])

        if 0 <= next_v[0] < n and 0 <= next_v[1] < m and matrix[next_v[0]][next_v[1]] != 1:
            v = next_v
        else:
            break

print(answer)