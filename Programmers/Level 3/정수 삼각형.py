from copy import deepcopy


def solution(triangle: list[list[int]]) -> int:
    n = len(triangle)
    dp = deepcopy(triangle)

    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:
                dp[i][j] += dp[i - 1][j]
            elif j == i:
                dp[i][j] += dp[i - 1][j - 1]
            else:
                dp[i][j] += max(dp[i - 1][j - 1:j + 1])

    answer = max(dp[n - 1])

    return answer