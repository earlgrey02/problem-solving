import sys

input = sys.stdin.readline

n = int(input())
matrix = [[] for _ in range(4)]
summations = {}
count = 0

for _ in range(n):
    for i, j in enumerate(map(int, input().split())):
        matrix[i].append(j)

for i in matrix[0]:
    for j in matrix[1]:
        if i + j in summations:
            summations[i + j] += 1
        else:
            summations[i + j] = 1

for i in matrix[2]:
    for j in matrix[3]:
        count += summations.get(-(i + j), 0)

print(count)