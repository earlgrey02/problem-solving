def solution(triangle):
    n = len(triangle)
    dp = [row[:] for row in triangle]

    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:
                dp[i][j] += dp[i - 1][j]
            elif j == i:
                dp[i][j] += dp[i - 1][j - 1]
            else:
                dp[i][j] += max(dp[i - 1][j - 1:j + 1])

    answer = max(dp[-1])

    return answer