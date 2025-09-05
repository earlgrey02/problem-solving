import sys
from math import isqrt

input = sys.stdin.readline

n, k = map(int, input().split())
divisors = set()

for i in range(1, isqrt(n) + 1):
    if n % i == 0:
        divisors.add(i)
        divisors.add(n // i)

print(divisors[k - 1] if len(divisors := sorted(list(divisors))) >= k else 0)