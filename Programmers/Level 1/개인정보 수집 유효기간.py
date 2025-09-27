def solution(today, terms, privacies):
    def get_day(date):
        year, month, day = tuple(map(int, date.split('.')))

        return year * 12 * 28 + month * 28 + day

    today = get_day(today)
    terms = dict(tuple(term.split()) for term in terms)
    privacies = [tuple(privacy.split()) for privacy in privacies]
    answer = []

    for i in range(len(privacies)):
        day = get_day(privacies[i][0])
        term = int(terms[privacies[i][1]]) * 28
        expired_day = day + term

        if expired_day <= today:
            answer.append(i + 1)

    return answer