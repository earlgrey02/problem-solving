import sys
from collections import Counter
from itertools import accumulate

input = sys.stdin.readline

t = int(input())
n = int(input())
sequences = []
sequences.append(list(map(int, input().split())))
m = int(input())
sequences.append(list(map(int, input().split())))
prefix_sums = [[0] + list(accumulate(sequence)) for sequence in sequences]
subtotals = [[prefix_sum[j] - prefix_sum[i] for i in range(len(prefix_sum)) for j in range(i + 1, len(prefix_sum))] for prefix_sum in prefix_sums]
counter = Counter(subtotals[0])

print(sum(counter[t - subtotal] for subtotal in subtotals[1]))