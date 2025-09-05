import sys
from math import isqrt

input = sys.stdin.readline

def sieve_of_eratosthenes(n: int) -> list[bool]:
    is_primes = [i > 1 for i in range(n + 1)]

    for i in range(2, isqrt(n) + 1):
        if is_primes[i]:
            for j in range(i ** 2, n + 1, i):
                is_primes[j] = False

    return is_primes

m, n = (int(input()) for _ in range(2))
is_primes = sieve_of_eratosthenes(n)

if numbers := [i for i in range(m, n + 1) if is_primes[i]]:
    print(sum(numbers), numbers[0], sep = '\n')
else:
    print(-1)