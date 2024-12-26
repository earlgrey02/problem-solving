from collections import Counter
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
words = [input().strip() for _ in range(n)]
counter = Counter(words)

print(*sorted(filter(lambda x: len(x) >= m, set(words)), key = lambda x: (-counter[x], -len(x), x)), sep = '\n')