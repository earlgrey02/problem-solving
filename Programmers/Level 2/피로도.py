from itertools import permutations


def solution(k, dungeons):
    answer = 0

    for case in permutations(dungeons, len(dungeons)):
        fatigue = k
        count = 0

        for dungeon in case:
            if dungeon[0] <= fatigue:
                fatigue -= dungeon[1]
                count += 1

        answer = max(answer, count)

    return answer