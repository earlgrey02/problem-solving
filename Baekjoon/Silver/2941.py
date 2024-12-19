import sys

input = sys.stdin.readline

word = input().strip()
alphabets = ("c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z=")

for alphabet in alphabets:
    word = word.replace(alphabet, "_")

print(len(word))