import sys

input = sys.stdin.readline

n = int(input())
prime_factors = []
d = 2

if n != 1:
    while d <= n:
        if n % d == 0:
            prime_factors.append(d)
            n //= d
        else:
            d += 1

    print(*prime_factors, sep = '\n')