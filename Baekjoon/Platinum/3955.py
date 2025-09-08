import sys
from math import inf

input = sys.stdin.readline

def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return (a, 1, 0)
    else:
        gcd, x, y = extended_gcd(b, a % b)

        return (gcd, y, x - (a // b) * y)

t = int(input())

for _ in range(t):
    k, c = map(int, input().split())
    gcd, x, _ = extended_gcd(c, k)
    x %= k

    if (k == 1 and c == 1) or c == 1:
        x = k + 1
    elif k == 1:
        x = 1
    elif gcd != 1:
        x = inf

    print(x if x <= 10 ** 9 else "IMPOSSIBLE")