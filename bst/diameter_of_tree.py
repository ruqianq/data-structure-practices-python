# Given the root of a binary tree, return the length of the diameter of the tree.
#
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
#
# The length of a path between two nodes is represented by the number of edges between them.
from typing import Optional

from bst.treenode import TreeNode


def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
    ans = 0

    def depth(p):
        nonlocal ans
        if not p: return 0
        left, right = depth(p.left), depth(p.right)
        ans = max(ans, left + right)
        return 1 + max(left, right)

    depth(root)
    return ans
