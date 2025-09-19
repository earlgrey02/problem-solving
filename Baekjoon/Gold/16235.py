import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
nutrients = [list(map(int, input().split())) for _ in range(n)]
matrix = [[5 for _ in range(n)] for _ in range(n)]
trees = [[{} for _ in range(n)] for _ in range(n)]
dy = (1, -1, 0, 0, 1, -1, 1, -1)
dx = (0, 0, 1, -1, 1, 1, -1, -1)

for _ in range(m):
    x, y, z = map(int, input().split())
    trees[x - 1][y - 1][z] = 1

for _ in range(k):
    for i in range(n):
        for j in range(n):
            next_trees = {}
            remains = 0

            for age, count in sorted(trees[i][j].items(), key = lambda x: x[0]):
                if (lived_count := min(matrix[i][j] // age, count)) > 0:
                    next_trees[age + 1] = lived_count
                    matrix[i][j] -= age * lived_count

                remains += (age // 2) * (count - lived_count)

            trees[i][j] = next_trees
            matrix[i][j] += nutrients[i][j] + remains

    for i in range(n):
        for j in range(n):
            for age, count in trees[i][j].items():
                if age % 5 == 0:
                    for l in range(8):
                        next_tree = (i + dy[l], j + dx[l])

                        if 0 <= next_tree[0] < n and 0 <= next_tree[1] < n:
                            trees[next_tree[0]][next_tree[1]][1] = trees[next_tree[0]][next_tree[1]].get(1, 0) + count

print(sum(sum(trees[i][j].values()) for i in range(n) for j in range(n)))