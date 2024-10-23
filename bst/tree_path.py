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


def to_linked_list_by_depth_dfs(node: TreeNode, depth: int, linked_list_arr: list):
    if node is None:
        return
    linked_list = LinkedList()
    if len(linked_list_arr) == depth:
        linked_list_arr.append(linked_list)
    else:
        linked_list = linked_list_arr[depth]
    linked_list.append(node.value)
    to_linked_list_by_depth_dfs(node.left, depth + 1, linked_list_arr)
    to_linked_list_by_depth_dfs(node.right, depth + 1, linked_list_arr)


def convert_binary_tree_to_linked_list_by_depth_dfs(root: TreeNode) -> list:
    linked_list_arr = []

    to_linked_list_by_depth_dfs(root, 0, linked_list_arr)
    return linked_list_arr


def binary_tree_paths(root: TreeNode) -> list:
    paths = []
    if not root:
        return paths

    dfs(root, '', paths)

    return paths


"""
with mutable slate
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def all_paths_of_a_binary_tree(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    # Algo: DSF, recurssive, top - buttom, pre-order
    # Trade off: unbalance tree O(n)
    # edge case: empty tree
    result = []
    if not root: return []
    def helper(node, slate):
        
        
        if not node.left and not node.right:
            result.append(slate[:])
        
        if node.left:
            slate.append(node.left.value)
            helper(node.left, slate)
            slate.pop()

        if node.right:
            slate.append(node.right.value)
            helper(node.right, slate)
            slate.pop()

    helper(root, [root.value])
    return result
