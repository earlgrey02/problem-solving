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

n = int(input())
is_primes = sieve_of_eratosthenes(n)
sequence = [i for i in range(n + 1) if is_primes[i]]
left, right = 0, 0
summation = sequence[0] if sequence else 0
count = 0

while True:
    if summation > n:
        summation -= sequence[left]
        left += 1
    elif summation < n:
        right += 1

        if right >= len(sequence):
            break

        summation += sequence[right]
    else:
        count += 1
        summation -= sequence[left]
        left += 1
        right += 1

        if right >= len(sequence):
            break

        summation += sequence[right]

print(count)