import sys

input = sys.stdin.readline

def pow(a: int, n: int):
    global c

    if n == 0:
        return 1
    else:
        b = pow(a, n // 2)

        return ((b ** 2) * (a if n % 2 != 0 else 1)) % c

a, b, c = map(int, input().split())

print(pow(a, b))