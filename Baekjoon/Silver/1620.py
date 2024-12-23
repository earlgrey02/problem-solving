import sys

input = sys.stdin.readline

n, m = map(int, input().split())
collection = dict()

for i in range(n):
    name = input().strip()

    collection[i + 1] = name
    collection[name] = i + 1

quizzes = [input().strip() for _ in range(m)]

print(*(collection[int(i) if i.isdigit() else i] for i in quizzes), sep = '\n')