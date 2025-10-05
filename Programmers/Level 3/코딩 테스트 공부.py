from math import inf


def solution(alg, cod, problems):
    max_alg, max_cod = max(max(problem[0] for problem in problems), alg), max(max(problem[1] for problem in problems), cod)
    dp = [[0 if i == alg and j == cod else inf for j in range(max_cod + 1)] for i in range(max_alg + 1)]
    problems.extend(([0, 0, 1, 0, 1], [0, 0, 0, 1, 1]))

    for i in range(alg, max_alg + 1):
        for j in range(cod, max_cod + 1):
            for problem in problems:
                if i >= problem[0] and j >= problem[1]:
                    next_alg, next_cod = min(i + problem[2], max_alg), min(j + problem[3], max_cod)
                    dp[next_alg][next_cod] = min(dp[next_alg][next_cod], dp[i][j] + problem[4])

    answer = dp[-1][-1]

    return answer