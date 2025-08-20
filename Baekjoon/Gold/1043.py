import sys

input = sys.stdin.readline

def union(v1: int, v2: int):
    v1, v2 = find(v1), find(v2)

    if v1 != v2:
        if ranks[v1] == ranks[v2]:
            parents[v2] = v1
            ranks[v1] += 1
        elif ranks[v1] < ranks[v2]:
            parents[v1] = v2
        else:
            parents[v2] = v1

def find(v: int) -> int:
    if parents[v] != v:
        parents[v] = find(parents[v])

    return parents[v]

n, m = map(int, input().split())
_, *true_people = map(int, input().split())
parents = [i for i in range(n + 1)]
ranks = [0 for _ in range(n + 1)]
parties = []
answer = 0

for _ in range(m):
    count, *people = map(int, input().split())
    parties.append(people)

    if count > 1:
        for i, j in zip(people, people[1:]):
            union(i, j)

true_people = set(find(i) for i in true_people)

for party in parties:
    if not next((i for i in party if find(i) in true_people), False):
        answer += 1

print(answer)