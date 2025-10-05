def solution(survey, choices):
    n = len(survey)
    scores = {}
    kinds = (('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N'))
    scores = {i: 0 for kind in kinds for i in kind}

    for i in range(n):
        if choices[i] < 4:
            scores[survey[i][0]] += 4 - choices[i]
        elif choices[i] > 4:
            scores[survey[i][1]] += choices[i] - 4

    answer = ''.join(max(kind, key = lambda x: scores[x]) for kind in kinds)

    return answer