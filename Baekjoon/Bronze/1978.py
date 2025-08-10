import sys
from math import floor, sqrt

input = sys.stdin.readline

_ = int(input())
numbers = list(map(int, input().split()))
maximum = max(numbers)
primes = [i > 1 for i in range(maximum + 1)]

for i in range(2, floor(sqrt(maximum)) + 1):
    if primes[i]:
        for j in range(i * 2, maximum + 1, i):
            primes[j] = False

print(len([True for i in numbers if primes[i]]))