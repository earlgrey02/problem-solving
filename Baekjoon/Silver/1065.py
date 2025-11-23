import sys

input = sys.stdin.readline

n = int(input())

print(sum(1 for i in range(1, n + 1) if i < 100 or int(str(i)[1]) - int(str(i)[0]) == int(str(i)[2]) - int(str(i)[1])))