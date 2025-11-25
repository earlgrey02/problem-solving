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
    print(root, end = '')

while True:
    try:
        preorder, inorder = map(list, input().split())
        inorder_indexes = {number: i for i, number in enumerate(inorder)}

        postorder_traversal((0, len(preorder) - 1), (0, len(inorder) - 1))
        print()
    except (EOFError, ValueError):
        break