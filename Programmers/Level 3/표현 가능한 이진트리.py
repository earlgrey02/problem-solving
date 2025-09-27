from math import ceil, log


def solution(numbers):
    def check_tree(tree, is_dummy = False):
        mid = len(tree) // 2

        if is_dummy and tree[mid] == 1:
            return False

        return len(tree) == 1 or all(check_tree(subtree, tree[mid] == 0) for subtree in (tree[:mid], tree[mid + 1:]))

    answer = []

    for number in numbers:
        n = len(bit := bin(number)[2:]) + 1
        tree = [0 for _ in range(2 ** ceil(log(n, 2)) - n)] + list(map(int, bit))

        answer.append(int(check_tree(tree)))

    return answer