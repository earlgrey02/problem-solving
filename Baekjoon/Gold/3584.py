import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    parents = [0 for _ in range(n)]
    has_parents = [False for _ in range(n)]
    visited = [False for _ in range(n)]

    for _ in range(n - 1):
        v1, v2 = map(lambda x: int(x) - 1, input().split())
        parents[v2] = v1
        has_parents[v2] = True

    root = next(i for i in range(n) if not has_parents[i])
    v1, v2 = map(lambda x: int(x) - 1, input().split())

    while True:
        visited[v1] = True

        if v1 == root:
            break

        v1 = parents[v1]

    while not visited[v2]:
        v2 = parents[v2]

    print(v2 + 1)