import sys

input = sys.stdin.readline

n, m = (int(input()) for _ in range(2))
broken_buttons = set(map(int, input().split()))
working_buttons = {i for i in range(10) if i not in broken_buttons}
count = abs(n - 100)

for i in range(1000001):
    if all(int(j) in working_buttons for j in str(i)):
        count = min(count, len(str(i)) + abs(i - n))

print(count)