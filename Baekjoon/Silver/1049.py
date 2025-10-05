import sys
from math import ceil

input = sys.stdin.readline

n, m = map(int, input().split())
costs = [tuple(map(int, input().split())) for _ in range(m)]
package, single = tuple(map(min, zip(tuple(map(int, input().split())) for _ in range(m))))

print(min(package * (n // 6) + single * (n % 6), package * ceil(n / 6), single * n))