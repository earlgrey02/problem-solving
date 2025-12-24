import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    string = input().strip()
    left, right = 0, len(string) - 1
    palindrome_number = 0

    while left < right:
        if string[left] == string[right]:
            left += 1
            right -= 1
        else:
            substrings = [string[:mid] + string[mid + 1:] for mid in (left, right)]
            palindrome_number = 1 if any(substring == substring[::-1] for substring in substrings) else 2
            break

    print(palindrome_number)