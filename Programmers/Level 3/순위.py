def solution(n: int, results: list[list[int]]) -> int:
    def floyd_warshall():
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if adjacencies[i][k] == 1 and adjacencies[k][j] == 1:
                        adjacencies[i][j] = 1
                    elif adjacencies[i][k] == -1 and adjacencies[k][j] == -1:
                        adjacencies[i][j] = -1

    adjacencies = [[0 for _ in range(n)] for _ in range(n)]

    for v1, v2 in results:
        adjacencies[v1 - 1][v2 - 1] = 1
        adjacencies[v2 - 1][v1 - 1] = -1

    floyd_warshall()

    answer = len([True for row in adjacencies if row.count(0) == 1])

    return answer