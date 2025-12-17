import sys
from collections import deque

input = sys.stdin.readline

def bfs(v: list[int]):
    queue = deque([v])
    visited[v[0]][v[1]][v[2]] = True

    while queue:
        v = queue.popleft()

        for i in range(3):
            for j in range(3):
                if i == j:
                    continue

                next_v = v[:]
                amount = min(v[i], capacities[j] - v[j])
                next_v[i] -= amount
                next_v[j] += amount

                if not visited[next_v[0]][next_v[1]][next_v[2]]:
                    visited[next_v[0]][next_v[1]][next_v[2]] = True
                    queue.append(next_v)

a, b, c = map(int, input().split())
visited = [[[False for _ in range(c + 1)] for _ in range(b + 1)] for _ in range(a + 1)]
capacities = (a, b, c)

bfs([0, 0, c])

print(*sorted(j for i in range(b + 1) for j in range(c + 1) if i != j and visited[0][i][j]))