from collections import Counter
from statistics import mean
import sys

input = sys.stdin.readline

n = int(input())
numbers = [int(input()) for _ in range(n)]
counter = Counter(numbers).most_common()
modes = list(map(lambda x: x[0], filter(lambda x: x[1] >= counter[0][1], counter)))

print(round(mean(numbers)))
print(sorted(numbers)[n // 2])
print(sorted(modes)[1] if len(modes) > 1 else modes[0])
print(max(numbers) - min(numbers))