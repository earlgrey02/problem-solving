import sys

input = sys.stdin.readline

def bellman_ford() -> bool:
    distances = [0 for _ in range(n + 1)]

    for i in range(n):
        for j in range(2 * m + h):
            v, next_v, w = edges[j]

            if distances[v] + w < distances[next_v]:
                if i == n - 1:
                    return False
                else:
                    distances[next_v] = distances[v] + w

    return True

t = int(input())

for _ in range(t):
    n, m, h = map(int, input().split())
    edges = []

    for _ in range(m):
        v1, v2, w = map(int, input().split())
        edges.append((v1, v2, w))
        edges.append((v2, v1, w))

    for _ in range(h):
        start, end, w = map(int, input().split())
        edges.append((start, end, -w))

    print("YES" if not bellman_ford() else "NO")