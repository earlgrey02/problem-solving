import sys

input = sys.stdin.readline

def sieve_of_eratosthenes(n: int, k: int) -> int:
    is_primes = [i > 1 for i in range(n + 1)]
    order = 0

    for i in range(2, n + 1):
        if is_primes[i]:
            for j in range(i, n + 1, i):
                if is_primes[j]:
                    is_primes[j] = False

                    if (order := order + 1) == k:
                        return j

    return 1

n, k = map(int, input().split())

print(sieve_of_eratosthenes(n, k))