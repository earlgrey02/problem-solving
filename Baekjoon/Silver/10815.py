import sys

input = sys.stdin.readline

_ = int(input())
cards = set(map(int, input().split()))
_ = int(input())

print(*(int(i in cards) for i in map(int, input().split())))