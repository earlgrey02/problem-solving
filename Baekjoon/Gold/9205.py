import sys
from collections import deque

input = sys.stdin.readline

def bfs(v: tuple[int, int]):
    queue = deque([v])
    visited[v] = True

    while queue:
        v = queue.popleft()

        if sum(abs(v[i] - destination[i]) for i in range(2)) <= 1000:
            return True

        for next_v in stores:
            if next_v not in visited and sum(abs(v[i] - next_v[i]) for i in range(2)) <= 1000:
                visited[next_v] = True
                queue.append(next_v)

    return False

t = int(input())

for _ in range(t):
    n = int(input())
    start = tuple(map(int, input().split()))
    stores = [tuple(map(int, input().split())) for _ in range(n)]
    destination = tuple(map(int, input().split()))
    visited = {}

    print("happy" if bfs(start) else "sad")