import sys

input = sys.stdin.readline

n = int(input())
numbers = sorted(map(int, input().split()))
count = 0

for i in range(n):
    left, right = 0, n - 1

    while left < right:
        if right == i or numbers[left] + numbers[right] > numbers[i]:
            right -= 1
        elif left == i or numbers[left] + numbers[right] < numbers[i]:
            left += 1
        else:
            count += 1
            break

print(count)