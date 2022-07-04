# Given the root of a binary tree, return all root-to-leaf paths in any order.
#
# A leaf is a node with no children.
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


def to_linked_list_by_depth_dfs(node: TreeNode, depth: int, linked_list: LinkedList, linked_list_arr: list):
    linked_list.append(node.value)
    if linked_list.length == depth:
        linked_list_arr.append(linked_list)

    if node.left and linked_list.length <= depth:
        to_linked_list_by_depth_dfs(node.left, depth, linked_list, linked_list_arr)
    if node.right and linked_list.length <= depth:
        to_linked_list_by_depth_dfs(node.right, depth, linked_list, linked_list_arr)


def convert_binary_tree_to_linked_list_by_depth_dfs(root: TreeNode, depth: int) -> list:
    linked_list_arr = []
    if not root:
        return linked_list_arr
    to_linked_list_by_depth_dfs(root, depth, LinkedList(), linked_list_arr)
    return linked_list_arr


def binary_tree_paths(root: TreeNode) -> list:
    paths = []
    if not root:
        return paths

    dfs(root, '', paths)

    return paths
