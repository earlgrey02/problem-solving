import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def tarjan(v: int) -> int:
    global label

    labels[v] = parent = (label := label + 1)
    stack.append(v)

    for next_v in adjacencies[v]:
        if labels[next_v] == -1:
            parent = min(parent, tarjan(next_v))
        elif not finished[next_v]:
            parent = min(parent, labels[next_v])

    if parent == labels[v]:
        scc = []
        next_v = -1

        while next_v != v:
            finished[next_v := stack.pop()] = True
            scc.append(next_v)

        sccs.append(scc)

    return parent

n, m = map(int, input().split())
adjacencies = [[] for _ in range(n + 1)]
labels = [-1 for _ in range(n + 1)]
finished = [False for _ in range(n + 1)]
stack = []
sccs = []
label = 0

for _ in range(m):
    start, end = map(int, input().split())
    adjacencies[start].append(end)

for i in range(1, n + 1):
    if labels[i] == -1:
        tarjan(i)

print("Yes" if len(sccs) == 1 else "No")