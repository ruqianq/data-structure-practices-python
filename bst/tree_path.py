# Given the root of a binary tree, return all root-to-leaf paths in any order.
#
# A leaf is a node with no children.
from typing import Optional, List

from bst.tree_node import TreeNode
from link_list.linked_list import LinkedList


def dfs(node: TreeNode, path: str, paths: list):
    path += str(node.value)
    if not node.left and not node.right:
        paths.append(path)

    if node.left:
        dfs(node.left, path + '->', paths)

    if node.right:
        dfs(node.right, path + '->', paths)


def convert_node_to_linked_list_by_depth_dfs(node: TreeNode, depth) -> [LinkedList]:
    if TreeNode is None:
        return []

    linked_list_arr = []
    start_linked_list_node = LinkedList(node.value)

    def helper(n: TreeNode, d):
        linked_list_arr.append(start_linked_list_node)
        d += 1
        if n.left and d <= depth:
            start_linked_list_node.next = n.left
            helper(n.left, d)
        if n.right and d <= depth:
            start_linked_list_node.next = n.right
            helper(n.right, d)
        helper(node, 0)

    return linked_list_arr


def binary_tree_paths(root: Optional[TreeNode]) -> List[str]:
    paths = []
    if not root:
        return paths

    dfs(root, '', paths)

    return paths
