import sys

input = sys.stdin.readline

n = int(input())
switches = list(map(int, input().split()))
m = int(input())

for _ in range(m):
    gender, index = map(int, input().split())

    if gender == 1:
        for i in range(index - 1, n, index):
            switches[i] = 1 - switches[i]
    elif gender == 2:
        index -= 1
        i = 0

        while 0 <= index - i and index + i < n and switches[index - i] == switches[index + i]:
            switches[index - i], switches[index + i] = 1 - switches[index - i], 1 - switches[index + i]
            i += 1

for i in range(0, n, 20):
    print(*map(int, switches[i:i + 20]))