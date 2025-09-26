import sys

input = sys.stdin.readline

def cantor_set(n: int) -> str:
    if n == 0:
        return '-'

    left, right = (cantor_set(n - 1) for _ in range(2))

    return left + ' ' * (3 ** (n - 1)) + right

while True:
    try:
        n = int(input())

        print(cantor_set(n))
    except (EOFError, ValueError):
        break