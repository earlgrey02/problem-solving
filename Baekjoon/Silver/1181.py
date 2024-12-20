import sys

input = sys.stdin.readline

n = int(input())
words = {input().strip() for _ in range(n)}

print(*sorted(words, key = lambda x: (len(x), x)), sep = '\n')