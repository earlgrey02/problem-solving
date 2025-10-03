def solution(commands):
    def union(v1, v2):
        v1, v2 = find(v1), find(v2)

        if v1 != v2:
            if table[v1[0]][v1[1]]:
                table[v2[0]][v2[1]] = None
                parents[v2[0]][v2[1]] = v1
            else:
                table[v1[0]][v1[1]] = None
                parents[v1[0]][v1[1]] = v2

    def find(v):
        if parents[v[0]][v[1]] != v:
            parents[v[0]][v[1]] = find(parents[v[0]][v[1]])

        return parents[v[0]][v[1]]

    table = [[None for _ in range(51)] for _ in range(51)]
    parents = [[(i, j) for j in range(51)] for i in range(51)]
    ranks = [[0 for _ in range(51)] for _ in range(51)]
    answer = []

    for command in commands:
        operator, *operands = command.split()

        if operator == 'UPDATE':
            if len(operands) == 3:
                r, c = find(tuple(map(int, operands[:2])))
                table[r][c] = operands[2]
            else:
                value1, value2 = operands

                for i in range(51):
                    for j in range(51):
                        if table[i][j] == value1:
                            table[i][j] = value2
        elif operator == 'MERGE':
            r1, c1, r2, c2 = map(int, operands)
            union((r1, c1), (r2, c2))
        elif operator == 'UNMERGE':
            r, c = map(int, operands)
            root = find((r, c))
            value = table[root[0]][root[1]]
            cells = []

            for i in range(51):
                for j in range(51):
                    if find((i, j)) == root:
                        cells.append((i, j))

            for v in cells:
                table[v[0]][v[1]] = None
                parents[v[0]][v[1]] = v

            table[r][c] = value
        elif operator == 'PRINT':
            r, c = find(tuple(map(int, operands)))
            answer.append(table[r][c] if table[r][c] else "EMPTY")

    return answer