import sys
from math import ceil

input = sys.stdin.readline

n = int(input())
tshirts = list(map(int, input().split()))
t, p = map(int, input().split())

print(sum(ceil(tshirt / t) for tshirt in tshirts))
print(n // p, n % p)