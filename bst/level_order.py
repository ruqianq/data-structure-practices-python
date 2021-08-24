# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

from collections import deque
from typing import Optional, List

from bst.treenode import TreeNode


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    if not root: return []
    queue, res = deque([root]), []

    while len(queue) > 0:
        cur_level, size = [], len(queue)
        for i in range(size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            cur_level.append(node.val)
        res.append(cur_level)
    return res
