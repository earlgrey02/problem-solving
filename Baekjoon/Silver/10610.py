import sys

input = sys.stdin.readline

n = sorted(input().strip(), reverse = True)

print(''.join(n) if '0' in n and sum(map(int, n)) % 3 == 0 else -1)