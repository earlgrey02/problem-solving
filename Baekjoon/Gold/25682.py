import sys
from math import inf

input = sys.stdin.readline

n, m, k = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
prefix_sum = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
answer = inf

for i in range(1, n + 1):
    for j in range(1, m + 1):
        cost = ((i + j) & 1) ^ (board[i - 1][j - 1] == 'W')
        prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + cost

for i in range(n - k + 1):
    for j in range(m - k + 1):
        answer = min(answer, (total := prefix_sum[i + k][j + k] - prefix_sum[i][j + k] - prefix_sum[i + k][j] + prefix_sum[i][j]), k * k - total)

print(answer)