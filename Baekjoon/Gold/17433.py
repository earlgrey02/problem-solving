import sys
from math import gcd

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    numbers = list(map(int, input().split()))
    differences = [abs(numbers[i] - numbers[i + 1]) for i in range(n - 1)]
    g = differences[0]

    for i in differences[1:]:
        g = gcd(g, i)

    print(g if g > 0 else "INFINITY")