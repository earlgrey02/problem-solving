def solution(n, computers):
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

    answer = 0
    parents = [i for i in range(n)]
    ranks = [0 for _ in range(n)]

    for i in range(n):
        for j in range(i, n):
            if i != j and computers[i][j] == 1:
                union(i, j)

    answer = len(set(find(i) for i in range(n)))

    return answer