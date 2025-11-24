import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def postorder_traversal(preorder: list[int]):
    if not preorder:
        return

    root = preorder[0]
    mid = next((i for i, j in enumerate(preorder[1:], 1) if j > root), len(preorder))

    postorder_traversal(preorder[1:mid])
    postorder_traversal(preorder[mid:])
    print(root)

preorder = []

while True:
    try:
        preorder.append(int(input()))
    except (EOFError, ValueError):
        break

postorder_traversal(preorder)