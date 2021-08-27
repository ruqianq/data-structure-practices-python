# Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different
# nodes in the tree.
from typing import Optional, List

from bst.treenode import TreeNode


def min_diff_in_bst(root: Optional[TreeNode]) -> int:
    diffs = []
    dsf(root, diffs)
    min_value = float('inf')
    for i in range(len(diffs) - 1):
        min_value = min(diffs[i+1] - diffs[i])
    return min_value


def dsf(node: TreeNode, diffs: List):
    if not node:
        return
    if node.left:
        dsf(node.left, diffs)
    diffs.append(node.value)
    if node.right:
        dsf(node.right, diffs)
