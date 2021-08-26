# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that
# adding up all the values along the path equals targetSum.
#
# A leaf is a node with no children.
from typing import Optional

from bst.treenode import TreeNode


def has_path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
    if not root:
        return False
    remains = target_sum - root.value
    if remains == 0 and not root.left and not root.right:
        return True
    return has_path_sum(root.left, remains) or has_path_sum(root.right, remains)


