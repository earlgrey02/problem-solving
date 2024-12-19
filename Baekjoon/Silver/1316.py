import sys

input = sys.stdin.readline

n = int(input())
words = (input().strip() for _ in range(n))
count = 0

for word in words:
    is_group = True

    for letter in word:
        letter_count = word.count(letter)

        if (letter_count > 1 and letter * letter_count not in word):
            is_group = False
            break

    if is_group:
        count += 1

print(count)