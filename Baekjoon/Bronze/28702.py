import sys

input = sys.stdin.readline

strings = (input().strip() for _ in range(3))
n = next(int(string) + 3 - i for i, string in enumerate(strings) if string.isdigit())

if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)