import sys

input = sys.stdin.readline

n, m = (int(input()) for _ in range(2))
materials = sorted(map(int, input().split()))
left, right = 0, n - 1
count = 0

while left < right:
    if (value := materials[left] + materials[right]) == m:
        count += 1
        left += 1
        right -= 1
    elif value < m:
        left += 1
    else:
        right -= 1

print(count)