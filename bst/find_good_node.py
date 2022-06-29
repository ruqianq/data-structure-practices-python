# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
#
# Return the number of good nodes in the binary tree.
from .tree_node import TreeNode


def helper(node, max_val) -> int:
    if not node:
        return 0
    counter = 0
    if node.value >= max_val:
        max_val = node.value
        counter = 1
    counter += helper(node.left, max_val)
    counter += helper(node.right, max_val)
    return counter


def count_good_nodes(root: TreeNode) -> int:
    return 1 + helper(root.left, root.value) + helper(root.right, root.value)
