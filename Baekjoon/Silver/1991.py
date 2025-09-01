import sys

input = sys.stdin.readline

def preorder_traversal(root: str) -> list[str]:
    if root == '.':
        return []
    else:
        return [root, *preorder_traversal(tree[root][0]), *preorder_traversal(tree[root][1])]

def inorder_traversal(root: str) -> list[str]:
    if root == '.':
        return []
    else:
        return [*inorder_traversal(tree[root][0]), root, *inorder_traversal(tree[root][1])]

def postorder_traversal(root: str) -> list[str]:
    if root == '.':
        return []
    else:
        return [*postorder_traversal(tree[root][0]), *postorder_traversal(tree[root][1]), root]

n = int(input())
tree = {}
root = 'A'

for _ in range(n):
    parent, *childs = input().split()
    tree[parent] = childs

print(*preorder_traversal(root), sep = '')
print(*inorder_traversal(root), sep = '')
print(*postorder_traversal(root), sep = '')