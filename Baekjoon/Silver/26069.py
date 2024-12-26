import sys

input = sys.stdin.readline

n = int(input())
records = set(["ChongChong"])

for _ in range(n):
    names = input().split()

    if any(name in records for name in names):
        records.update(names)

print(len(records))