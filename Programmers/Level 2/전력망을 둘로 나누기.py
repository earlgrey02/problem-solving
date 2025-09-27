from collections import Counter
from math import inf


def solution(n, wires):
    def union(v1, v2):
        v1, v2 = find(v1), find(v2)

        if v1 != v2:
            if ranks[v1] == ranks[v2]:
                parents[v2] = v1
                ranks[v1] += 1
            elif ranks[v1] < ranks[v2]:
                parents[v1] = v2
            else:
                parents[v2] = v1

    def find(v):
        if parents[v] != v:
            parents[v] = find(parents[v])

        return parents[v]

    answer = inf

    for i in range(len(wires)):
        parents = [i for i in range(n)]
        ranks = [0 for _ in range(n)]

        for j in range(len(wires)):
            if i != j:
                start, end = wires[j]
                union(start - 1, end - 1)

        counter = Counter(find(i) for i in range(n))
        answer = min(answer, max(counter.values()) - min(counter.values()))

    return answer