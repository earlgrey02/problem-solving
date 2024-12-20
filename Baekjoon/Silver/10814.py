import sys

input = sys.stdin.readline

n = int(input())
users = map(lambda x: (x[0], int(x[1][0]), x[1][1]), enumerate(input().split() for _ in range(n)))

print(*(f"{i[1]} {i[2]}" for i in sorted(users, key = lambda x: (x[1], x[0]))), sep = '\n')