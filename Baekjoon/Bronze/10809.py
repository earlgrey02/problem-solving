import sys

input = sys.stdin.readline

word = input().strip()

for i in range(ord('a'), ord('z') + 1):
    print(word.find(chr(i)), end = " ")