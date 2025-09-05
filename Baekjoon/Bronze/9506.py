import sys
from math import isqrt

input = sys.stdin.readline

while (n := int(input())) != -1:
    divisors = set()

    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)

    divisors = sorted(divisors - {n})

    print(f"{n} = {" + ".join(map(str, divisors))}" if sum(divisors) == n else f"{n} is NOT perfect.")