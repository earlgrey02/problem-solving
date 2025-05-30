import sys

input = sys.stdin.readline

n, k = map(int, input().split())
sequence = list(map(int, input().split()))
left, right = 0, k - 1
prefix_sum = maximum = sum(sequence[left:right + 1])

while right < n - 1:
    prefix_sum -= sequence[left]
    left += 1
    right += 1
    prefix_sum += sequence[right]

    maximum = max(maximum, prefix_sum)

print(maximum)