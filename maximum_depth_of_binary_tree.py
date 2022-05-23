from typing import List


tree1 = [3, 9, 20, None, None, 15, 71]
tree2 = [1, None, 2]

def maximum_depth(Tree: List) -> int:
    level = 0
    count = 0
    max_node = 1

    for node in Tree:
        count += 1
        if count == max_node:
            level += 1
            count = 0
            max_node = 2 ** level

    return level


# print(maximum_depth(tree1))
# print(maximum_depth(tree2))

