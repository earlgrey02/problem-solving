from math import sqrt, floor
import sys

input = sys.stdin.readline

numbers = []

while (n := int(input())) != 0:
    numbers.append(n)

maximum = max(numbers)
primes = [i > 1 for i in range(maximum * 2 + 1)]

for i in range(2, floor(sqrt(maximum * 2)) + 1):
    if primes[i]:
        for j in range(i * 2, maximum * 2 + 1, i):
            primes[j] = False

print(*(len(list(filter(lambda x: x, primes[i + 1:2 * i + 1]))) for i in numbers), sep = '\n')