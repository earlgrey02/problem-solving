def solution(n: int, tops: list[int]) -> int:
    dp = [[0 for _ in range(2)] for _ in range(n)]
    dp[0] = [1, 2 + tops[0]]

    for i in range(1, n):
        dp[i][0] = sum(dp[i - 1]) % 10007
        dp[i][1] = ((1 + tops[i]) * dp[i - 1][0] + (2 + tops[i]) * dp[i - 1][1]) % 10007

    answer = sum(dp[n - 1]) % 10007

    return answer