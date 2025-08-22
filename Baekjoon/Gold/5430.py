import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    functions = input().strip()
    n = int(input())
    array = deque(input().strip()[1:-1].split(','))

    if n == 0:
        array = deque()

    is_error = False
    reversed_count = 0

    for i in functions:
        if i == 'R':
            reversed_count += 1
        else:
            if not array:
                is_error = True
                break
            else:
                if reversed_count % 2 == 0:
                    array.popleft()
                else:
                    array.pop()

    if is_error:
        print("error")
    else:
        if reversed_count % 2 != 0:
            array.reverse()

        print(f"[{','.join(array)}]")