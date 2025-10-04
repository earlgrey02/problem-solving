import sys

input = sys.stdin.readline

def tarjan(v: int) -> int:
    global label

    labels[v] = parent = (label := label + 1)
    stack.append(v)

    for next_v in range(n):
        if adjacencies[v][next_v] == 1:
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

n = int(input())
costs = list(map(int, input().split()))
adjacencies = [list(map(int, input().strip())) for _ in range(n)]
labels = [-1 for _ in range(n)]
finished = [False for _ in range(n)]
stack = []
sccs = []
label = 0

for i in range(n):
    if labels[i] == -1:
        tarjan(i)

print(sum(min(costs[v] for v in scc) for scc in sccs))