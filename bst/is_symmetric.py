# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
from typing import Optional
from bst.tree_node import TreeNode

# recursive approach
# Space complexity varies:
# Time complexity: O(n) - n is the number of nodes
# Recursive: O(h) - better for balanced trees
def is_mirror(node1, node2):
    if node1 and node2:
        return is_mirror(node1.left, node2.right) and is_mirror(node1.right, node2.left)
    else:
        return node1 == node2


def is_symmetric(root: Optional[TreeNode]) -> bool:
    if root.left and root.right:
        return is_mirror(root.left, root.right) and root.left.val == root.right.val
    if not root.left and not root.right:
        return True
    if (root.left and not root.right) or (not root.left and root.right):
        return False

# interative approach
# Space complexity: O(n) - n is the number of nodes
# Time complexity: O(n) - n is the number of nodes

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def check_if_symmetric(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     bool
    """
    # Write your code here.
    # Algo: Level by level, BFS, two queue to track left sub tree and right sub tree
    # trade off: if sym, T: O(n) space logn. if not sym, O(1) ~ O(n)
    # edge case: empty tree; or one node
    
    if not root: return True
    
    q_left = [root]
    q_right = [root]
    
    while len(q_left) > 0 and len(q_right) > 0:
        node_left = q_left.pop(0)
        node_right = q_right.pop(0)
        # Check values match
        if node_left.value != node_right.value:
            return False
        # Check left side of left subtree vs right side of right subtree
        if node_left.left is None and node_right.right is not None:
            return False
        if node_left.left is not None and node_right.right is None:
            return False
        if node_left.left and node_right.right:
            q_left.append(node_left.left)
            q_right.append(node_right.right)
            
        # Check right side of left subtree vs left side of right subtree
        if node_left.right is None and node_right.left is not None:
            return False
        if node_left.right is not None and node_right.left is None:
            return False
        if node_left.right and node_right.left:
            q_left.append(node_left.right)
            q_right.append(node_right.left)
            
    return True
