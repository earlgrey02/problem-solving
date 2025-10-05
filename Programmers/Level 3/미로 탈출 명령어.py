import sys

sys.setrecursionlimit(10 ** 6)

def solution(n, m, x, y, r, c, k):
    def backtracking(v, path = ''):
        nonlocal answer

        distance = sum(abs(i - j) for i, j in zip(v, (r - 1, c - 1)))
        remain = k - len(path)

        if len(path) == k and v == (r - 1, c - 1):
            answer = path
        elif answer == "impossible" and distance <= remain and (distance - remain) % 2 == 0:
            for i in range(4):
                next_v = (v[0] + dy[i], v[1] + dx[i])

                if 0 <= next_v[0] < n and 0 <= next_v[1] < m and not visited[next_v[0]][next_v[1]][k - (len(path) + 1)]:
                    visited[next_v[0]][next_v[1]][k - (len(path) + 1)] = True
                    backtracking(next_v, path + directions[i])

    visited = [[[False for _ in range(k + 1)] for _ in range(m)] for _ in range(n)]
    directions = ('d', 'l', 'r', 'u')
    dy = (1, 0, 0, -1)
    dx = (0, -1, 1, 0)
    answer = "impossible"

    backtracking((x - 1, y - 1))

    return answer