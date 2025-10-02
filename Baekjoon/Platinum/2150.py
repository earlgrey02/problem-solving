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

v, e = map(int, input().split())
adjacencies = [[] for _ in range(v + 1)]
labels = [-1 for _ in range(v + 1)]
finished = [False for _ in range(v + 1)]
stack = []
sccs = []
label = 0

for _ in range(e):
    start, end = map(int, input().split())
    adjacencies[start].append(end)

for i in range(1, v + 1):
    if labels[i] == -1:
        tarjan(i)

print(len(sccs))

for scc in sorted(map(sorted, sccs)):
    print(*sorted(scc) + [-1], sep = ' ')