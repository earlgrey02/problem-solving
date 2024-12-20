import sys

input = sys.stdin.readline

matrix = [list(input().strip()) for _ in range(5)]
max_len = max(map(lambda x: len(x), matrix))

for j in range(max_len):
    for i in range(5):
        if j < len(row := matrix[i]):
            print(row[j], end = '')