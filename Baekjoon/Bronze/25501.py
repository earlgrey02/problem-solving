import sys

input = sys.stdin.readline

def recursion(string: str, start: int, end: int) -> int:
    counts[string] += 1

    if start >= end:
        return 1
    elif string[start] != string[end]:
        return 0
    else:
        return recursion(string, start + 1, end - 1)

def isPalindrome(string: str) -> int:
    return recursion(string, 0, len(string) - 1)

t = int(input())
strings = [input().strip() for _ in range(t)]
counts = {string: 0 for string in strings}

print(*(f"{isPalindrome(string)} {counts[string]}" for string in strings), sep = '\n')