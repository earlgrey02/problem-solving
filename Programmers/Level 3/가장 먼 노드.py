from collections import deque


def solution(n, edges):
    def bfs(v):
        queue = deque([v])
        visited[v] = 1

        while queue:
            v = queue.popleft()

            for next_v in adjacencies[v]:
                if visited[next_v] == 0:
                    visited[next_v] = visited[v] + 1
                    queue.append(next_v)

    adjacencies = [[] for _ in range(n + 1)]
    visited = [0 for _ in range(n + 1)]

    for v1, v2 in edges:
        adjacencies[v1].append(v2)
        adjacencies[v2].append(v1)

    bfs(1)

    answer = visited.count(max(visited))

    return answer