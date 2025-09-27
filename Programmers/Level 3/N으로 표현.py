def solution(n, number):
    dp = [set() for _ in range(8)]
    answer = -1

    for i in range(8):
        dp[i].add(int(str(n) * (i + 1)))

        for j in range(i):
            for k in dp[j]:
                for l in dp[i - j - 1]:
                    dp[i].add(k + l)
                    dp[i].add(k - l)
                    dp[i].add(k * l)

                    if l != 0:
                        dp[i].add(k // l)

        if number in dp[i]:
            answer = i + 1
            break

    return answer