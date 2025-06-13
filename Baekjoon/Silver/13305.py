import sys

input = sys.stdin.readline

n = int(input())
distances = list(map(int, input().split()))
costs = list(map(int, input().split()))
min_cost = costs[0]
answer = 0

for i in range(n - 1):
    min_cost = min(min_cost, costs[i])
    answer += min_cost * distances[i]

print(answer)