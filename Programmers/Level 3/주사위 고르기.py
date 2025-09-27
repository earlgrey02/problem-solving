from bisect import bisect_left
from collections import defaultdict
from itertools import combinations, product


def solution(dices):
    n = len(dices)
    summations = defaultdict(list)
    max_win = 0

    for dice_case in combinations(range(n), n // 2):
        for number_case in product(*(dices[i] for i in dice_case)):
            summations[dice_case].append(sum(number_case))

    for summation in summations.values():
        summation.sort()

    for dice_case in summations.keys():
        opponent_case = tuple(i for i in range(n) if i not in dice_case)
        win = sum(bisect_left(summations[opponent_case], summation) for summation in summations[dice_case])

        if max_win < win:
            max_win = win
            answer = tuple(map(lambda x: x + 1, dice_case))

    return answer