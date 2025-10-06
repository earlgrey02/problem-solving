from collections import defaultdict
from math import ceil


def solution(fees, records):
    parkings = {}
    durations = defaultdict(int)
    answer = []
    end = 23 * 60 + 59

    for record in records:
        time, number, status = record.split()
        number = int(number)
        hour, minute = map(int, time.split(':'))
        minute += hour * 60

        if status == "IN":
            parkings[number] = minute
        elif status == "OUT":
            durations[number] += minute - parkings[number]
            parkings.pop(number)

    for number, minute in parkings.items():
        durations[number] += end - minute

    for number, duration in sorted(durations.items(), key = lambda x: int(x[0])):
        cost = fees[1]

        if duration > fees[0]:
            cost += ceil((duration - fees[0]) / fees[2]) * fees[3]

        answer.append(cost)

    return answer