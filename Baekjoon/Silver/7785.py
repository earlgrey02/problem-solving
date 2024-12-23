import sys

input = sys.stdin.readline

n = int(input())
names = set()

for _ in range(n):
    name, operator = input().split()

    if operator == 'enter':
        names.add(name)
    else:
        names.remove(name)

print(*sorted(names, reverse = True), sep = '\n')