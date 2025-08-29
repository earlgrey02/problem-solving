import sys

input = sys.stdin.readline

while (n := input().strip()) != '0':
    print("yes" if n == n[::-1] else "no")