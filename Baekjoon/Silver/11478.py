import sys

input = sys.stdin.readline

s = input().strip()
strings = {s[i:j + 1] for i in range(len(s)) for j in range(len(s))}

print(len(strings) - 1)