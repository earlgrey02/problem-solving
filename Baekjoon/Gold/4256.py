import sys

input = sys.stdin.readline

def postorder_traversal(preorder_range: tuple[int, int], inorder_range: tuple[int, int]):
    if any(start > end for start, end in (preorder_range, inorder_range)):
        return

    root = preorder[preorder_range[0]]
    mid = inorder_indexes[root]
    left_size = mid - inorder_range[0] - 1

    postorder_traversal((preorder_range[0] + 1, preorder_range[0] + left_size + 1), (inorder_range[0], mid - 1))
    postorder_traversal((preorder_range[0] + left_size + 2, preorder_range[1]), (mid + 1, inorder_range[1]))
    print(root, end = ' ')

t = int(input())

for _ in range(t):
    n = int(input())
    preorder, inorder = (list(map(int, input().split())) for _ in range(2))
    inorder_indexes = {number: i for i, number in enumerate(inorder)}

    postorder_traversal((0, n - 1), (0, n - 1))
    print()