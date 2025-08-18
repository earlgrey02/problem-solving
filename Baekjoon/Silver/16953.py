import sys
from collections import defaultdict, deque

input = sys.stdin.readline

def bfs(v: int) -> int:
    queue = deque([v])
    visited[v] = 1

    while queue:
        v = queue.popleft()

        if v == b:
            return visited[v]

        for next_v in (v * 2, int(str(v) + '1')):
            if a < next_v <= b and visited[next_v] == 0:
                visited[next_v] = visited[v] + 1
                queue.append(next_v)

    return -1

a, b = map(int, input().split())
visited = defaultdict(int)

print(bfs(a))