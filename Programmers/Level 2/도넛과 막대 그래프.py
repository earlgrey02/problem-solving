from collections import defaultdict


def solution(edges: list[list[int]]) -> list[int]:
    degrees = defaultdict(lambda: [0, 0])
    answer = [0 for _ in range(4)]

    for start, end in edges:
        degrees[start][1] += 1
        degrees[end][0] += 1

    for v, degree in degrees.items():
        if degree[0] == 0 and degree[1] >= 2:
            answer[0] = v
        elif degree[0] > 0 and degree[1] == 0:
            answer[2] += 1
        elif degree[0] >= 2 and degree[1] >= 2:
            answer[3] += 1

    answer[1] = degrees[answer[0]][1] - sum(answer[2:])

    return answer