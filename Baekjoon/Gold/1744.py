import sys

input = sys.stdin.readline

n = int(input())
sequence = [int(input()) for _ in range(n)]
positives = sorted([i for i in sequence if i > 1], reverse = True)
negatives = sorted(i for i in sequence if i <= 0)
summation = sequence.count(1)

for numbers in (positives, negatives):
    summation += sum(numbers[i] * numbers[i + 1] if i + 1 < len(numbers) else numbers[i] for i in range(0, len(numbers), 2))

print(summation)