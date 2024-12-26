import sys

input = sys.stdin.readline

n = int(input())
records = set()
count = 0

for _ in range(n):
    nickname = input().strip()

    if nickname == "ENTER":
        records.clear()
    elif nickname not in records:
        count += 1
        records.add(nickname)

print(count)