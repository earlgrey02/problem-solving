from itertools import combinations


def solution(friends: list[str], gifts: list[str]) -> int:
    adjacencies = {friend: {friend: 0 for friend in friends} for friend in friends}
    received_gifts = {friend: 0 for friend in friends}

    for a, b in map(lambda x: x.split(), gifts):
        adjacencies[a][b] += 1
        adjacencies[b][a] -= 1

    for a, b in combinations(friends, 2):
        if adjacencies[a][b] != 0:
            received_gifts[a if adjacencies[a][b] > adjacencies[b][a] else b] += 1
        else:
            a_point, b_point = (sum(adjacencies[i].values()) for i in (a, b))

            if a_point != b_point:
                received_gifts[a if a_point > b_point else b] += 1

    answer = max(received_gifts.values())

    return answer