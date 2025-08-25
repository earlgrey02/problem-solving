import sys

input = sys.stdin.readline

n = int(input())

print(str(bin(n)).count('1'))