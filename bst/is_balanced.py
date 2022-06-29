# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as:
#
# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
from typing import Optional

from bst.get_height import get_height, check_height_and_balanced
from bst.tree_node import TreeNode


def is_balanced(root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    left_sub_tree_height = get_height(root.left)
    right_sub_tree_height = get_height(root.right)
    return abs(left_sub_tree_height - right_sub_tree_height) <= 1 and is_balanced(root.right) and is_balanced(root.left)


def check_balanced(root: Optional[TreeNode]) -> bool:
    if check_height_and_balanced(root) == -1:
        return False
    else:
        return True
