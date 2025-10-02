import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
counter = Counter(sorted(input().strip() for _ in range(n)))

print(counter.most_common()[0][0])