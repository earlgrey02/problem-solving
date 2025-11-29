import sys

input = sys.stdin.readline

def dfs(v: int) -> int:
    visited[v] = True
    count = 0

    if not adjacencies[v]:
        count = 1
    else:
        for next_v in adjacencies[v]:
            if not visited[next_v]:
                count += dfs(next_v)

    return count

n = int(input())
adjacencies = [[] for _ in range(n)]
visited = [False for _ in range(n)]

for end, start in enumerate(map(int, input().split())):
    if start == -1:
        root = end
    else:
        adjacencies[start].append(end)

deleted_v = int(input())
adjacencies = [list(filter(lambda x: x != deleted_v, adjacency)) for adjacency in adjacencies]

print(dfs(root) if root != deleted_v else 0)