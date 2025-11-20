import sys
from math import isqrt

input = sys.stdin.readline

def dfs(v: int):
    if len(str(v)) == n:
        magic_primes.append(v)
    else:
        for i in range(10):
            next_v = v * 10 + i

            if next_v > 1 and all(next_v % i != 0 for i in range(2, isqrt(next_v) + 1)):
                dfs(next_v)

n = int(input())
primes = (2, 3, 5, 7)
magic_primes = []

for prime in primes:
    dfs(prime)

print(*magic_primes, sep = '\n')