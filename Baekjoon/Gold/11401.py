import sys

input = sys.stdin.readline

n, k = map(int, input().split())
p = int(1e9 + 7)

def factorial(x: int) -> int:
    result = 1

    for i in range(2, x + 1):
        result = (result * i) % p

    return result

print((factorial(n) * pow(factorial(n - k) * factorial(k), p - 2, p)) % p)