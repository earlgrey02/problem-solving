import sys
from math import inf

input = sys.stdin.readline

def floyd_warshall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

n = int(input())
distances = [[inf if i != j else 0 for j in range(n)] for i in range(n)]

while (members := tuple(map(int, input().split()))) != (-1, -1):
    start, end = members
    distances[start - 1][end - 1] = 1
    distances[end - 1][start - 1] = 1

floyd_warshall()

scores = [max(distances[i]) for i in range(n)]

print(candidate_score := min(scores), scores.count(candidate_score))
print(*(i + 1 for i in range(n) if scores[i] == candidate_score))