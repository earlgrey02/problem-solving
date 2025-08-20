import sys
from collections import deque

input = sys.stdin.readline

def bidirectional_bfs(start: int, end: int) -> list[str]:
    start_visited = {start: []}
    end_visited = {end: []}
    start_queue = deque([start])
    end_queue = deque([end])

    while start_queue and end_queue:
        for _ in range(len(start_queue)):
            v = start_queue.popleft()

            for operator, next_v in (('D', v * 2 % 10000), ('S', (v - 1) % 10000), ('L', v // 1000 + (v % 1000) * 10), ('R', v // 10 + (v % 10) * 1000)):
                if next_v not in start_visited:
                    start_visited[next_v] = [*start_visited[v], operator]

                    if next_v in end_visited:
                        return start_visited[next_v] + end_visited[next_v]

                    start_queue.append(next_v)

        for _ in range(len(end_queue)):
            v = end_queue.popleft()
            reversed_operators = [('S', (v + 1) % 10000), ('L', v // 10 + (v % 10) * 1000), ('R', v // 1000 + (v % 1000) * 10)]

            if v % 2 == 0:
                reversed_operators = [('D', v // 2), ('D', v // 2 + 5000), *reversed_operators]

            for operator, next_v in reversed_operators:
                if next_v not in end_visited:
                    end_visited[next_v] = [operator, *end_visited[v]]

                    if next_v in start_visited:
                        return start_visited[next_v] + end_visited[next_v]

                    end_queue.append(next_v)

    return []

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    print(*bidirectional_bfs(a, b), sep = '')