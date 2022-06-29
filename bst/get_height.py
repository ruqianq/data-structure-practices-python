from typing import Optional

from bst.tree_node import TreeNode


def get_height(node: TreeNode) -> int:
    if not node:
        return 0
    return max(get_height(node.left), get_height(node.right)) + 1


def check_height_and_balanced(node: Optional[TreeNode]) -> int:
    if not node:
        return 0
    left_height = check_height_and_balanced(node.left)

    if left_height == -1:
        return -1

    right_height = check_height_and_balanced(node.right)

    if right_height == -1:
        return -1

    height_diff = left_height - right_height

    if abs(height_diff) > 1:
        return -1
    else:
        return max(left_height, right_height) + 1
