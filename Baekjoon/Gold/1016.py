import sys
from math import ceil, isqrt

input = sys.stdin.readline

def sieve_of_eratosthenes(start: int, end: int) -> list[bool]:
    is_squares = [False for _ in range(end - start + 1)]

    for i in range(2, isqrt(end) + 1):
        for j in range((square := i ** 2) * ceil(start / square), end + 1, square):
            is_squares[j - start] = True

    return is_squares

start, end = map(int, input().split())
is_squares = sieve_of_eratosthenes(start, end)

print(is_squares.count(False))