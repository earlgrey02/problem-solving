def solution(n, info):
    def dfs(count, counts):
        nonlocal answer, max_diff

        if len(counts) == 11:
            total_scores = [0, 0]

            if count > 0:
                counts[-1] = count

            for i in range(11):
                if info[i] > 0 or counts[i] > 0:
                    total_scores[int(info[i] < counts[i])] += 10 - i

            if (diff := total_scores[1] - total_scores[0]) > 0:
                if diff > max_diff:
                    answer = counts
                    max_diff = diff
                elif diff == max_diff:
                    for i in range(10, -1, -1):
                        if answer[i] != counts[i]:
                            if answer[i] < counts[i]:
                                answer = counts

                            break
        else:
            for i in (0, info[len(counts)] + 1):
                if count >= i:
                    dfs(count - i, counts + [i])

    max_diff = 0
    answer = [-1]

    dfs(n, [])

    return answer