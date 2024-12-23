from math import gcd
import sys

input = sys.stdin.readline

n = int(input())
positions = [int(input()) for _ in range(n)]
intervals = [positions[i + 1] - positions[i] for i in range(n - 1)]
interval_gcd = gcd(*intervals)

print(sum(i // interval_gcd - 1 for i in intervals))