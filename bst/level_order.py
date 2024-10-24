from typing import Optional, List
from bst.tree_node import TreeNode


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Returns the level order traversal of a binary tree.

    Args:
        root (Optional[TreeNode]): The root node of the binary tree.

    Returns:
        List[List[int]]: The level order traversal of the binary tree.

    """
    if not root:
        return []
    ans, level = [], [root]
    while level:
        ans.append([node.val for node in level])
        temp = []
        for node in level:
            temp.extend([node.left, node.right])
        level = [leaf for leaf in temp if leaf]
    return ans


def bsf(node):
    """
    Performs breadth-first search traversal on a binary tree.

    Args:
        node: The root node of the binary tree.

    Returns:
        List[List[int]]: The level order traversal of the binary tree.

    """
    if not node:
        return
    queue = [node]
    result = []
    level = 0
    while queue:
        level_size = len(queue)
        level_nodes = []
        for _ in range(level_size):
            current = queue.pop(0)
            level_nodes.append(current.value)
            print(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        result.append(level_nodes)
        level += 1
    return result