import sys

input = sys.stdin.readline

array = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
word = input().strip()
time = 0

for letter in word:
    for i, string in enumerate(array):
        if letter in string:
            time += i + 3
            break

print(time)