import sys
from functools import reduce
from itertools import combinations

input = sys.stdin.readline

n, k = map(int, input().split())
word_bits = [reduce(lambda acc, x: acc | 1 << (ord(x) - ord('a')), input().strip(), 0) for _ in range(n)]
base_bit = reduce(lambda acc, x: acc | 1 << (ord(x) - ord('a')), ('a', 'c', 'i', 'n', 't'), 0)
count = 0

if k >= 5:
    for case in combinations((1 << i for i in range(26) if not (base_bit & 1 << i)), k - 5):
        learned_bit = base_bit | reduce(lambda acc, x: acc | x, case, 0)
        count = max(sum(1 for bit in word_bits if not (bit & ~learned_bit)), count)

print(count)