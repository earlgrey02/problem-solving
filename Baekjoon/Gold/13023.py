import sys

input = sys.stdin.readline

def backtracking(v: int, depth: int = 0):
    global is_present

    if depth == 4:
        is_present = True
    else:
        for next_v in adjacencies[v]:
            if not visited[next_v]:
                visited[next_v] = True
                backtracking(next_v, depth + 1)
                visited[next_v] = False

n, m = map(int, input().split())
adjacencies = [[] for _ in range(n)]
visited = [False for _ in range(n)]
is_present = False

for _ in range(m):
    v1, v2 = map(int, input().split())
    adjacencies[v1].append(v2)
    adjacencies[v2].append(v1)

for i in range(n):
    visited[i] = True
    backtracking(i)
    visited[i] = False

    if is_present:
        break

print(int(is_present))