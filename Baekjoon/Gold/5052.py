import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    numbers = sorted(input().strip() for _ in range(n))
    is_consistent = True

    for i in range(n - 1):
        if numbers[i + 1].startswith(numbers[i]):
            is_consistent = False
            break

    print("YES" if is_consistent else "NO")