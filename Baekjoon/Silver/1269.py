import sys

input = sys.stdin.readline

_ = map(int, input().split())

print(len(set(map(int, input().split())).symmetric_difference(map(int, input().split()))))