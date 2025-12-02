import sys

input = sys.stdin.readline

n, k = (int(input()) for _ in range(2))
sensors = sorted(map(int, input().split()))
distances = sorted((sensors[i + 1] - sensors[i] for i in range(n - 1)), reverse = True)

print(sum(distances[k - 1:]))