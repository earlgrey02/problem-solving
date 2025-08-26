import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
words = [list(reversed(input().strip())) for _ in range(n)]
values = defaultdict(int)
number = 9
summation = 0

for word in words:
    for i in range(len(word)):
        values[word[i]] += 10 ** i

for i in sorted(values.values(), reverse = True):
    summation += number * i
    number -= 1

print(summation)