import sys
from math import isqrt

input = sys.stdin.readline

def is_prime(n: int) -> bool:
    if n <= 1:
        return False

    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False

    return True

t = int(input())
numbers = [int(input()) for _ in range(t)]

for _ in range(t):
    n = int(input())

    while True:
        if is_prime(n):
            break
        else:
            n += 1

    print(n)