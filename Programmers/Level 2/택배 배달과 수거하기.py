def solution(cap, n, deliveries, pickups):
    remains = [0, 0]
    answer = 0

    for i in range(n - 1, -1, -1):
        remains[0] += deliveries[i]
        remains[1] += pickups[i]

        while any(remain > 0 for remain in remains):
            for j in range(2):
                remains[j] -= cap

            answer += (i + 1) * 2

    return answer