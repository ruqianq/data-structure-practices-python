# Given the root of a binary tree, return all root-to-leaf paths in any order.
#
# A leaf is a node with no children.
from typing import Optional, List

from bst.treenode import TreeNode


def dfs(node: TreeNode, path, paths):
    path += str(node.value)
    if not node.left and not node.right:
        paths.append(path)

    if node.left:
        dfs(node.left, path + '->', paths)

    if node.right:
        dfs(node.right, path + '->', paths)


def binary_tree_paths(root: Optional[TreeNode]) -> List[str]:
    paths = []
    if not root:
        return paths

    dfs(root, '', paths)

    return paths
