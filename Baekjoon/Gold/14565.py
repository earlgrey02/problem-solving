import sys

input = sys.stdin.readline

def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return (a, 1, 0)
    else:
        gcd, x, y = extended_gcd(b, a % b)

        return (gcd, y, x - (a // b) * y)

n, a = map(int, input().split())
gcd, x, y = extended_gcd(a, n)

print((n - a) % n, x % n if gcd == 1 else -1)