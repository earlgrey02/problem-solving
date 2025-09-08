import sys

input = sys.stdin.readline

def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return (a, 1, 0)
    else:
        gcd, x, y = extended_gcd(b, a % b)

        return (gcd, y, x - (a // b) * y)

t = int(input())

for _ in range(t):
    m, n, x, y = map(int, input().split())
    gcd, x0, _ = extended_gcd(m, n)

    if (y - x) % gcd != 0:
        print(-1)
    else:
        particular_x = x0 * ((y - x) // gcd)
        general_x = (particular_x % (n // gcd))
        k = m * general_x + x

        print(k if k != 0 else m * n)