import sys
from collections import deque

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

def topological_sort(indegrees: list[int]) -> bool:
    queue = deque(i for i in range(len(sccs)) if indegrees[i] == 0)

    while queue:
        v = queue.popleft()

        if queue:
            return False

        for next_v in scc_adjacencies[v]:
            indegrees[next_v] -= 1

            if indegrees[next_v] == 0:
                queue.append(next_v)

    return True

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

scc_adjacencies = [[] for _ in range(len(sccs))]
scc_indegrees = [0 for _ in range(len(sccs))]
scc_indexes = [-1 for _ in range(n + 1)]

for i, scc in enumerate(sccs):
    for v in scc:
        scc_indexes[v] = i

for v in range(1, n + 1):
    for next_v in adjacencies[v]:
        if scc_indexes[v] != scc_indexes[next_v]:
            scc_adjacencies[scc_indexes[v]].append(scc_indexes[next_v])
            scc_indegrees[scc_indexes[next_v]] += 1

if topological_sort(scc_indegrees[:]):
    print(len(starts := sorted(v for i in range(len(sccs)) for v in sccs[i] if scc_indegrees[i] == 0)))
    print(*starts)
else:
    print(0)