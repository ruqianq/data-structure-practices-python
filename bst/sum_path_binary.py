# You are given the root of a binary tree where each node has a value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
#
# For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.
#
# Return the sum of these numbers. The answer is guaranteed to fit in a 32-bits integer.
from typing import Optional, List

from bst.tree_node import TreeNode


def dsf(node: TreeNode, cur_path: str, sums: List):
    cur_path += str(node.value)
    if not node.left and not node.right:
        sums.append(int(cur_path, 2))
    if node.left:
        dsf(node.left, cur_path, sums)
    if node.right:
        dsf(node.right, cur_path, sums)


def sum_root_to_leaf(root: Optional[TreeNode]) -> int:
    sums = []
    if not root.left and not root.right:
        return root.value
    dsf(root, '', sums)
    return sum(sums)
