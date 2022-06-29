# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
#
# Note: A leaf is a node with no children.
from typing import Optional

from bst.tree_node import TreeNode


def min_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    if root.left and root.right:
        return min(min_depth(root.left), min_depth(root.right)) + 1
    if not root.right:
        return max(min_depth(root.left), min_depth(root.right)) + 1
    if not root.left:
        return max(min_depth(root.left), min_depth(root.right)) + 1
