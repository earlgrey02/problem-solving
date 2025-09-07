from itertools import permutations
from math import isqrt


def solution(numbers: str) -> int:
    def sieve_of_eratosthenes(n: int) -> list[bool]:
        is_primes = [i > 1 for i in range(n + 1)]

        for i in range(2, isqrt(n) + 1):
            if is_primes[i]:
                for j in range(i ** 2, n + 1, i):
                    is_primes[j] = False

        return is_primes

    candidates = set(int(''.join(case)) for i in range(len(numbers)) for case in permutations(numbers, i + 1))
    is_primes = sieve_of_eratosthenes(max(candidates))
    answer = sum(is_primes[candidate] for candidate in candidates)

    return answer