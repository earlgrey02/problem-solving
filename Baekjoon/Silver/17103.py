from math import sqrt, floor
import sys

input = sys.stdin.readline

t = int(input())
numbers = [int(input()) for _ in range(t)]
maximum = max(numbers)
primes = [i > 1 for i in range(maximum + 1)]

for i in range(2, floor(sqrt(maximum)) + 1):
    if primes[i]:
        for j in range(i * 2, maximum + 1, i):
            primes[j] = False

print(*(len(list(True for j in range(floor(i / 2) + 1) if primes[j] and primes[i - j])) for i in numbers), sep = '\n')