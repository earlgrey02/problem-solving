import sys

input = sys.stdin.readline

def merge_sort(array: list[int]) -> list[int]:
    if len(array) == 1:
        return array

    mid = (len(array) + 1) // 2
    left, right = merge_sort(array[:mid]), merge_sort(array[mid:])

    return merge(left, right)

def merge(left: list[int], right: list[int]):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            orders.append(left[i])
            i += 1
        else:
            result.append(right[j])
            orders.append(right[j])
            j += 1

    orders.extend(rest := left[i:] + right[j:])

    return result + rest

a, k = map(int, input().split())
array = list(map(int, input().split()))
orders = []

merge_sort(array)

print(orders[k - 1] if len(orders) >= k else -1)