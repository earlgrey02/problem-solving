import sys

input = sys.stdin.readline

def get_index(n: int, v: tuple[int, int]):
    if n == 0:
        return 0

    half = 2 ** (n - 1)
    size = half ** 2

    if v[0] < half and v[1] < half:
        return get_index(n - 1, v)
    elif v[0] < half and v[1] >= half:
        return size + get_index(n - 1, (v[0], v[1] - half))
    elif v[0] >= half and v[1] < half:
        return 2 * size + get_index(n - 1, (v[0] - half, v[1]))
    else:
        return 3 * size + get_index(n - 1, (v[0] - half, v[1] - half))

n, r, c = map(int, input().split())

print(get_index(n, (r, c)))