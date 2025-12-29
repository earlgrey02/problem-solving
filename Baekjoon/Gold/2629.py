import sys

input = sys.stdin.readline

n = int(input())
weights = list(map(int, input().split()))
_ = int(input())
queries = list(map(int, input().split()))
summation = sum(weights)
dp = [False for _ in range(summation + 1)]
dp[0] = True

for weight in weights:
    next_dp = dp[:]

    for i in range(summation + 1):
        if dp[i]:
            if i + weight <= summation:
                next_dp[i + weight] = True

            next_dp[abs(i - weight)] = True

    dp = next_dp

print(*('Y' if query <= summation and dp[query] else 'N' for query in queries))