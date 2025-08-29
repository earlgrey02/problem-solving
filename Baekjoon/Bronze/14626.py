import sys

input = sys.stdin.readline

number = input().strip()

for digit in range(10):
    if sum((1 if i % 2 == 0 else 3) * (int(j) if j != '*' else digit) for i, j in enumerate(number)) % 10 == 0:
        print(digit)
        break