import sys
from math import prod

input = sys.stdin.readline

def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return (a, 1, 0)
    else:
        gcd, x, y = extended_gcd(b, a % b)

        return (gcd, y, x - (a // b) * y)

def chinese_reminder_theorem(remainders: tuple[int, int, int], moduli: tuple[int, int, int]) -> int:
    mod = prod(moduli)

    return sum(i * (mod // j) * (extended_gcd(mod // j, j)[1] % j) for i, j in zip(remainders, moduli)) % mod

e, s, m = map(int, input().split())

print(year if (year := chinese_reminder_theorem((e, s, m), (15, 28, 19))) > 0 else 7980)