from itertools import product


def solution(users, emoticons):
    answer = [0, 0]

    for case in product((10 * (i + 1) for i in range(4)), repeat = len(emoticons)):
        discounted_emoticons = [(rate, cost * (1 - (rate / 100))) for cost, rate in zip(emoticons, case)]
        result = [0, 0]

        for thresholds in users:
            cost = sum(discounted_cost for rate, discounted_cost in discounted_emoticons if rate >= thresholds[0])

            if cost >= thresholds[1]:
                result[0] += 1
            else:
                result[1] += cost

        answer = max(answer, result, key = lambda x: (x[0], x[1]))

    return answer