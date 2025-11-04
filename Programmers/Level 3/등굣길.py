def solution(m, n, puddles):
    def dfs(v):
        if v == (n - 1, m - 1):
            return 1
        elif dp[v[0]][v[1]] != -1:
            return dp[v[0]][v[1]]
        else:
            dp[v[0]][v[1]] = 0

            for i in range(2):
                next_v = (v[0] + dy[i], v[1] + dx[i])

                if 0 <= next_v[0] < n and 0 <= next_v[1] < m and next_v not in puddles:
                    dp[v[0]][v[1]] += dfs(next_v)

        return dp[v[0]][v[1]] % mod

    dp = [[-1 for _ in range(m)] for _ in range(n)]
    puddles = {tuple(map(lambda x: x - 1, puddle[::-1])) for puddle in puddles}
    mod = int(1e9) + 7
    dy = (1, 0)
    dx = (0, 1)

    dfs((0, 0))

    answer = dp[0][0] % mod

    return answer