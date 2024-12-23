from math import sqrt, floor
import sys

input = sys.stdin.readline

m, n = map(int, input().split())
primes = [i > 1 for i in range(n + 1)]

for i in range(2, floor(sqrt(n)) + 1):
    if primes[i]:
        for j in range(i * 2, n + 1, i):
            primes[j] = False

print(*(i for i in range(m, n + 1) if primes[i]), sep = '\n')