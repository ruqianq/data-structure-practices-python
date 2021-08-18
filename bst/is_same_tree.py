# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
from typing import Optional
from.treenode import TreeNode


def helper(node1: TreeNode, node2: TreeNode):
    if node1 and node2 and node1.value == node2.value:
        return helper(node1.left, node2.left) and helper(node1.right, node2.right)
    else:
        return node1 == node2

def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

    return helper(p, q)
