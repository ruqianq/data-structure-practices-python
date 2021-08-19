# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as:
#
# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
from typing import Optional

from bst.treenode import TreeNode


def get_height(node: TreeNode) -> int:
    if not node:
        return 0
    height = max(get_height(node.left), get_height(node.right)) + 1
    return height


def is_balanced(root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    left_sub_tree_height = get_height(root.left)
    right_sub_tree_height = get_height(root.right)
    return abs(left_sub_tree_height - right_sub_tree_height) <= 1 and is_balanced(root.right) and is_balanced(root.left)
