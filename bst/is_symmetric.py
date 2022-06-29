# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
from typing import Optional
from bst.tree_node import TreeNode


def is_mirror(node1, node2):
    if node1 and node2:
        return is_mirror(node1.left, node2.right) and is_mirror(node1.right, node2.left)
    else:
        return node1 == node2


def is_symmetric(root: Optional[TreeNode]) -> bool:
    if root.left and root.right:
        return is_mirror(root.left, root.right) and root.left.val == root.right.val
    if not root.left and not root.right:
        return True
    if (root.left and not root.right) or (not root.left and root.right):
        return False
