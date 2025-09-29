import sys

input = sys.stdin.readline

string = input().strip()
m = int(input())
left, right = list(string), []

for _ in range(m):
    operator, *operand = input().split()

    if operator == 'L' and left:
        right.append(left.pop())
    elif operator == 'D' and right:
        left.append(right.pop())
    elif operator == 'B' and left:
        left.pop()
    elif operator == 'P':
        left.append(*operand)

print(*left, *right[::-1], sep = '')