import sys

input = sys.stdin.readline

def hanoi(n: int, start: int, end: int):
    if n == 1:
        print(start, end)
    else:
        hanoi(n - 1, start, 6 - start - end)
        print(start, end)
        hanoi(n - 1, 6 - start - end, end)

n = int(input())

print(2 ** n - 1)
hanoi(n, 1, 3)