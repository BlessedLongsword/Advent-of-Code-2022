import numpy as np


def get_forest(file):
    return np.asarray([[int(tree) for tree in list(line)] for line in open(file).read().splitlines()])


def visible_trees(forest):
    n_rows, n_cols = forest.shape
    visibles = 2 * (n_rows + n_cols - 2)
    tree_visibilities = {(i, j): [False, False, False, False]  \
                         for i in range(1, n_rows - 1) for j in range(1, n_cols - 1)}

    for i in range(1, forest.shape[0] - 1):
        row_max = forest[i].max()
        if forest[i, 0] == row_max:
            continue
        current_max = forest[i, 0]
        for j in range(1, forest.shape[1] - 1):
            if forest[i, j] == row_max:
                tree_visibilities[(i, j)][0] = True
                break
            elif forest[i, j] > current_max:
                tree_visibilities[(i, j)][0] = True
                current_max = forest[i, j]

    for i in range(1, forest.shape[0] - 1):
        row_max = forest[i].max()
        if forest[i, -1] == row_max:
            continue
        current_max = forest[i, -1]
        for j in range(forest.shape[1] - 2, 0, -1):
            if forest[i, j] == row_max:
                tree_visibilities[(i, j)][1] = True
                break
            elif forest[i, j] > current_max:
                tree_visibilities[(i, j)][2] = True
                current_max = forest[i, j]

    for j in range(1, forest.shape[1] - 1):
        column_max = forest[:, j].max()
        if forest[0, j] == column_max:
            continue
        current_max = forest[0, j]
        for i in range(1, forest.shape[0] - 1):
            if forest[i, j] == column_max:
                tree_visibilities[(i, j)][2] = True
                break
            elif forest[i, j] > current_max:
                tree_visibilities[(i, j)][2] = True
                current_max = forest[i, j]

    for j in range(1, forest.shape[1] - 1):
        column_max = forest[:, j].max()
        if forest[-1, j] == column_max:
            continue
        current_max = forest[-1, j]
        for i in range(forest.shape[0] - 2, 0, -1):
            if forest[i, j] == column_max:
                tree_visibilities[(i, j)][3] = True
                break
            elif forest[i, j] > current_max:
                tree_visibilities[(i, j)][3] = True
                current_max = forest[i, j]

    return visibles + sum(any(visibilities) for visibilities in tree_visibilities.values())


def get_scenic_score(forest, tree):
    tree_i, tree_j = tree
    scenic_score, direction_score = 1, 0

    for i in range(tree_i - 1, -1, -1):
        direction_score += 1
        if forest[i, tree_j] >= forest[tree_i, tree_j]:
            break

    scenic_score *= direction_score
    direction_score = 0

    for i in range(tree_i + 1, forest.shape[0]):
        direction_score += 1
        if forest[i, tree_j] >= forest[tree_i, tree_j]:
            break

    scenic_score *= direction_score
    direction_score = 0

    for j in range(tree_j - 1, -1, -1):
        direction_score += 1
        if forest[tree_i, j] >= forest[tree_i, tree_j]:
            break

    scenic_score *= direction_score
    direction_score = 0

    for j in range(tree_j + 1, forest.shape[1]):
        direction_score += 1
        if forest[tree_i, j] >= forest[tree_i, tree_j]:
            break

    scenic_score *= direction_score

    return scenic_score


def highest_scenic_score(forest):
    return max(get_scenic_score(forest, (i, j)) for i in range(forest.shape[0]) for j in range(forest.shape[1]))


print(visible_trees(get_forest('input.txt')))
print(highest_scenic_score(get_forest('input.txt')))
