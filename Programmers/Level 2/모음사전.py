from itertools import product


def solution(word):
    words = []

    for i in range(5):
        words.extend(map(''.join, product(('A', 'E', 'I', 'O', 'U'), repeat = i + 1)))

    answer = sorted(words).index(word) + 1

    return answer