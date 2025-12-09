import sys

input = sys.stdin.readline

def get_weights(student: int, v: tuple[int, int]) -> tuple[int, int]:
    weights = [0, 0]

    for k in range(4):
        next_v = (v[0] + dy[k], v[1] + dx[k])

        if 0 <= next_v[0] < n and 0 <= next_v[1] < n:
            if matrix[next_v[0]][next_v[1]] in pairs[student]:
                weights[0] += 1
            elif matrix[next_v[0]][next_v[1]] == -1:
                weights[1] += 1

    return tuple(weights)

n = int(input())
matrix = [[-1 for _ in range(n)] for _ in range(n)]
pairs = {}
score = 0
dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)

for _ in range(n ** 2):
    student, *students = map(int, input().split())
    pairs[student] = set(students)

for student in pairs:
    candidates = []

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == -1:
                weights = get_weights(student, v := (i, j))
                candidates.append((v, weights))

    v, _ = max(candidates, key = lambda x: (x[1], -x[0][0], -x[0][1]))
    matrix[v[0]][v[1]] = student

for i in range(n):
    for j in range(n):
        weight = get_weights(matrix[i][j], (i, j))[0]

        if weight > 0:
            score += 10 ** (weight - 1)

print(score)