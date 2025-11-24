import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def preorder_traversal(inorder_range: tuple[int, int], postorder_range: tuple[int, int]):
    if any(start > end for start, end in (inorder_range, postorder_range)):
        return

    root = postorder[postorder_range[1]]
    mid = inorder_indexes[root]
    left_size = mid - inorder_range[0] - 1

    print(root, end = ' ')
    preorder_traversal((inorder_range[0], mid - 1), (postorder_range[0], postorder_range[0] + left_size))
    preorder_traversal((mid + 1, inorder_range[1]), (postorder_range[0] + left_size + 1, postorder_range[1] - 1))

n = int(input())
inorder, postorder = (list(map(int, input().split())) for _ in range(2))
inorder_indexes = {v: i for i, v in enumerate(inorder)}

preorder_traversal(*((0, n - 1) for _ in range(2)))