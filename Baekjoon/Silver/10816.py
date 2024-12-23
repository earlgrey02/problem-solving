from collections import Counter
import sys

input = sys.stdin.readline

n = int(input())
counter = Counter(map(int, input().split()))
_ = int(input())

print(*(counter[i] for i in map(int, input().split())))