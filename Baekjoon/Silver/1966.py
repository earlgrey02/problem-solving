import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    documents = deque(enumerate(map(int, input().split())))
    order = 0

    while documents:
        if max(map(lambda x: x[1], documents)) <= (document := documents.popleft())[1]:
            order += 1

            if document[0] == m:
                break
        else:
            documents.append(document)

    print(order)