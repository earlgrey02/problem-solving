import sys
from collections import deque
from math import isqrt

input = sys.stdin.readline

def sieve_of_eratosthenes(n: int) -> list[bool]:
    is_primes = [i > 1 for i in range(n + 1)]

    for i in range(2, isqrt(n) + 1):
        if is_primes[i]:
            for j in range(i ** 2, n + 1, i):
                is_primes[j] = False

    return is_primes

def bfs(v: int, destination: int) -> int:
    queue = deque([v])
    visited = {v: 0}

    while queue:
        v = queue.popleft()

        if v == destination:
            return visited[v]

        for i in range(4):
            for j in range(10):
                if i == j == 0 or int(str(v)[i]) == j:
                    continue

                next_v = list(str(v))
                next_v[i] = str(j)
                next_v = int(''.join(next_v))

                if next_v not in visited and is_primes[next_v]:
                    visited[next_v] = visited[v] + 1
                    queue.append(next_v)

    return -1

t = int(input())
is_primes = sieve_of_eratosthenes(10 ** 4)

for _ in range(t):
    a, b = map(int, input().split())

    print(count if (count := bfs(a, b)) != -1 else "IMPOSSIBLE")