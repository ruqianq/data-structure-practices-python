# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array.
from typing import Optional, List

from bst.tree_node import TreeNode


def average_of_levels(root: Optional[TreeNode]) -> List[float]:
    ans, level = [], [root]
    while level:
        level_sum, count = 0, 0
        temp = []
        for node in level:
            level_sum += node.value
            count += 1
            temp.extend([node.left, node.right])
        ans.append(level_sum/count)
        level = [leaf for leaf in temp if leaf]
    return ans
