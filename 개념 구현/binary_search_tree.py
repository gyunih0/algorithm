
from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sorted_array_to_bst(lst):
    if not lst:
        return None

    mid = len(lst) // 2

    node = TreeNode(lst[mid])
    node.left = sorted_array_to_bst(lst[:mid])
    node.right = sorted_array_to_bst(lst[mid + 1:])

    return node


def make_lst_by_bst(root, limit):
    if not root:
        return []

    lst = []
    q = deque([root])

    while q:
        if len(lst) > limit:
            break

        node = q.popleft()
        if node:
            lst.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            lst.append(None)

    return lst


def test_sorted_array_to_bst(lst):
    if not lst:
        return []
    root = sorted_array_to_bst(lst)
    return make_lst_by_bst(root, len(lst))


assert test_sorted_array_to_bst(lst=[-10, -3, 0, 5, 9]) == [0, -3, 9, -10, None, 5]
assert test_sorted_array_to_bst(lst=[-10, -7, -3, -1, 0, 1, 4, 5, 7, 9]) == [1, -3, 7, -7, 0, 5, 9, -10, None, -1, None]