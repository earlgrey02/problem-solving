from math import sqrt, floor
import sys

input = sys.stdin.readline

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, floor(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

t = int(input())

for _ in range(t):
    n = int(input())

    while True:
        if is_prime(n):
            break
        else:
            n += 1

    print(n)