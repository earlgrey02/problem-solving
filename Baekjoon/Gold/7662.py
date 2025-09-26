import sys
from heapq import heappop, heappush

input = sys.stdin.readline

def sync():
    for heap in (max_heap, min_heap):
        while heap and heap[0][1] in deleted:
            heappop(heap)

t = int(input())

for _ in range(t):
    k = int(input())
    max_heap, min_heap = [], []
    deleted = set()

    for i in range(k):
        operator, operand = input().split()

        if operator == 'I':
            heappush(max_heap, (-int(operand), i))
            heappush(min_heap, (int(operand), i))
        elif operator == 'D':
            sync()

            if int(operand) == 1 and max_heap:
                deleted.add(heappop(max_heap)[1])
            elif int(operand) == -1 and min_heap:
                deleted.add(heappop(min_heap)[1])

    sync()

    print(*(-max_heap[0][0], min_heap[0][0]) if max_heap and min_heap else ("EMPTY",))