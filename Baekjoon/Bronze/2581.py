from math import sqrt, floor
import sys

input = sys.stdin.readline

m, n = (int(input()) for _ in range(2))
primes = [i > 1 for i in range(n + 1)]

for i in range(2, floor(sqrt(n)) + 1):
    if primes[i]:
        for j in range(i * 2, n + 1, i):
            primes[j] = False

if len(numbers := [i for i in range(m, n + 1) if primes[i]]) > 0:
    print(sum(numbers), numbers[0], sep = '\n')
else:
    print(-1)