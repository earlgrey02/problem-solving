from itertools import permutations


def solution(k: int, dungeons: list[list[int]]) -> int:
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