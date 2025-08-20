import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def preorder_to_postorder(nodes: list[int]):
    if len(nodes) == 0:
        return

    root = nodes[0]
    mid = next((i for i, j in enumerate(nodes[1:], 1) if j > root), len(nodes))

    preorder_to_postorder(nodes[1:mid])
    preorder_to_postorder(nodes[mid:])
    print(root)

nodes = []

while True:
    try:
        nodes.append(int(input()))
    except (EOFError, ValueError):
        break

preorder_to_postorder(nodes)