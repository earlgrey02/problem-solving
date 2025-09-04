import sys
from bisect import bisect_right

input = sys.stdin.readline

def union(v1: int, v2: int):
    v1, v2 = find(v1), find(v2)

    if v1 != v2:
        parents[v2] = v1

def find(v: int) -> int:
    if parents[v] != v:
        parents[v] = find(parents[v])

    return parents[v]

n, m, k = map(int, input().split())
cards = sorted(map(int, input().split()))
parents = [i for i in range(n + 1)]

for card in map(int, input().split()):
    union((parent := find(bisect_right(cards, card))) + 1, parent)

    print(cards[parent])