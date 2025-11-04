import sys

input = sys.stdin.readline

n, k = map(int, input().split())
mod = int(1e9) + 7

def factorial(n: int) -> int:
    result = 1

    for i in range(2, n + 1):
        result = (result * i) % mod

    return result

print((factorial(n) * pow(factorial(n - k) * factorial(k), mod - 2, mod)) % mod)