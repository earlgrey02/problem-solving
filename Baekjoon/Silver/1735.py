from fractions import Fraction
import sys

input = sys.stdin.readline

fraction = sum(Fraction(*map(int, input().split())) for _ in range(2))

print(fraction.numerator, fraction.denominator)