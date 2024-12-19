import sys

input = sys.stdin.readline

def print_star(i):
    global n

    for j in range(n - i - 1):
        print(" ", end = "")

    for j in range(2 * i + 1):
        print("*", end = "")

    print()

n = int(input())

for i in range(n):
    print_star(i)

for i in range(n - 2, -1, -1):
    print_star(i)