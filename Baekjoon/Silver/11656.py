import sys

input = sys.stdin.readline

string = input().strip()

print(*sorted(string[i:] for i in range(len(string))), sep = '\n')