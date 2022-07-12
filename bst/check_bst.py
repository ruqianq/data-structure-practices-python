# Check the bt is the bst
from bst.tree_node import TreeNode


def check_bst(root: TreeNode) -> bool:
    def helper(node: TreeNode, min_value: int or None, max_value: int or None) -> bool:
        if node is None:
            return True
        if (min_value is not None and min_value >= node.value) or (max_value is not None and max_value < node.value):
            return False
        if not helper(node.left, min_value, node.value) or not helper(node.right, node.value, max_value):
            return False
        return True
    return helper(root, None, None)
