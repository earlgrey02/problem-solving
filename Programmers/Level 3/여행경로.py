from collections import defaultdict


def solution(tickets):
    def backtracking(path):
        nonlocal answer

        if len(path) == len(tickets) + 1 and not answer:
            answer = path
        else:
            v = path[-1]

            for i in range(len(tickets)):
                next_v = tickets[i][1]

                if v == tickets[i][0] and not visited[i]:
                    visited[i] = True
                    backtracking([*path, next_v])
                    visited[i] = False

    answer = []
    tickets.sort()
    visited = [False for _ in range(len(tickets))]

    backtracking(["ICN"])

    return answer