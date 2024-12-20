from itertools import combinations
import sys

input = sys.stdin.readline

_, m = map(int, input().split())
cards = map(int, input().split())

print(sorted(filter(lambda x: x <= m , map(lambda x: sum(x), combinations(cards, 3))))[-1])