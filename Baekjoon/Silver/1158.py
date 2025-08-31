import sys

input = sys.stdin.readline

n, k = map(int, input().split())
sequence = [i for i in range(1, n + 1)]
result = []
k -= 1
i = k

while sequence:
    result.append(sequence.pop(i := i % len(sequence)))
    i += k

print(f"<{", ".join(map(str, result))}>")