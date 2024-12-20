from statistics import mean
import sys

input = sys.stdin.readline

numbers = [int(input()) for _ in range(5)]

print(int(mean(numbers)), sorted(numbers)[2], sep = '\n')