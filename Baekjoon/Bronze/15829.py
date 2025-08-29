import sys

input = sys.stdin.readline

l = int(input())
string = input().strip()
hash = 0
mod = 1234567891

for i, char in enumerate(string):
    hash = (hash + ((ord(char) - ord('a') + 1) * (31 ** i))) % mod

print(hash)