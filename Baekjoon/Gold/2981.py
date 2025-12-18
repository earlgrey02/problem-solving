import sys
from math import gcd, isqrt

input = sys.stdin.readline

n = int(input())
numbers = [int(input()) for _ in range(n)]
differences = [abs(numbers[i] - numbers[i + 1]) for i in range(n - 1)]
g = differences[0]
m = set()

for i in differences[1:]:
    g = gcd(g, i)

for i in range(2, isqrt(g) + 1):
    if g % i == 0:
        m.add(i)
        m.add(g // i)

m.add(g)

print(*sorted(m))