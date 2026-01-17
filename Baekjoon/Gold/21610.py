import sys

input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
clouds = [(i, j) for i in range(n - 2, n) for j in range(2)]
dy = (0, -1, -1, -1, 0, 1, 1, 1)
dx = (-1, -1, 0, 1, 1, 1, 0, -1)

for _ in range(m):
    d, distance = map(int, input().split())
    d -= 1

    for i in range(len(clouds)):
        clouds[i] = tuple(map(lambda x: x % n, (clouds[i][0] + dy[d] * distance, clouds[i][1] + dx[d] * distance)))
        matrix[clouds[i][0]][clouds[i][1]] += 1

    for v in clouds:
        for i in range(1, 8, 2):
            next_v = (v[0] + dy[i], v[1] + dx[i])

            if 0 <= next_v[0] < n and 0 <= next_v[1] < n and matrix[next_v[0]][next_v[1]] > 0:
                matrix[v[0]][v[1]] += 1

    before_clouds = set(clouds)
    clouds.clear()

    for i in range(n):
        for j in range(n):
            if (i, j) not in before_clouds and matrix[i][j] >= 2:
                matrix[i][j] -= 2
                clouds.append((i, j))

print(sum(map(sum, matrix)))