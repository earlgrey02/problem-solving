from math import sqrt, floor
import sys

input = sys.stdin.readline

while (n := int(input())) != -1:
    divisors = set()

    for i in range(1, floor(sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)

    divisors = sorted(list(divisors - {n}))

    print(f"{n} = {" + ".join(map(str, divisors))}" if sum(divisors) == n else f"{n} is NOT perfect.")