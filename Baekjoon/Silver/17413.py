import sys

input = sys.stdin.readline

string = input().strip()
tokens = string.replace('>', '<').split('<')
result = []

for i in range(len(tokens)):
    if i % 2 == 0:
        result.append(' '.join(word[::-1] for word in tokens[i].split()))
    else:
        result.append(f"<{tokens[i]}>")

print(*result, sep = '')