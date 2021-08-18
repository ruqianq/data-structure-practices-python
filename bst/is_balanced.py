# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as:
#
# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
from typing import Optional

from bst.treenode import TreeNode


def get_height(node: TreeNode) -> int:
    left_height = 1
    right_height = 1
    if not node:
        return 0
    left_height += get_height(node.left)
    right_height += get_height(node.right)

    height = max(left_height, right_height)
    return height


def is_balanced(self, root: Optional[TreeNode]) -> bool:
    if not root.left or not root.right:
        return True
    if not root.left and root.right:
        return False
    if root.left and not root.right:
        return False
    return