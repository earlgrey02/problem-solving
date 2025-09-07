from collections import deque


def solution(matrix: list[list[int]]) -> int:
    def bfs(v: tuple[int, int]):
        queue = deque([v])
        visited[v[0]][v[1]] = 1

        while queue:
            v = queue.popleft()

            for i in range(4):
                next_v = (v[0] + dy[i], v[1] + dx[i])

                if 0 <= next_v[0] < n and 0 <= next_v[1] < m and matrix[next_v[0]][next_v[1]] == 1 and visited[next_v[0]][next_v[1]] == -1:
                    visited[next_v[0]][next_v[1]] = visited[v[0]][v[1]] + 1
                    queue.append(next_v)

    n, m = len(matrix), len(matrix[0])
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    dy = (1, -1, 0, 0)
    dx = (0, 0, 1, -1)

    bfs((0, 0))

    return visited[n - 1][m - 1]