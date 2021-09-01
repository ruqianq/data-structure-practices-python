from bst.treenode import TreeNode


def get_height(node: TreeNode) -> int:
    if not node:
        return 0
    return max(get_height(node.left), get_height(node.right)) + 1
