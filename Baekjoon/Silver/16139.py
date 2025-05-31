import sys

input = sys.stdin.readline

string = input().strip()
q = int(input())
prefix_sum = []
counts = {i: 0 for i in map(chr, range(ord('a'), ord('z') + 1))}

for i in string:
    counts[i] += 1
    prefix_sum.append(counts.copy())

for _ in range(q):
    a, i, j = input().split()
    i, j = map(int, (i, j))

    print(prefix_sum[j][a] - (prefix_sum[i - 1][a] if i > 0 else 0))