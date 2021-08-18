# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
#
# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
#
from typing import List, Optional

from .treenode import TreeNode


def sorted_array_to_bst(nums: List[int]) -> Optional[TreeNode]:
    if len(nums) == 1:
        return TreeNode(nums[0])
    cur = round(len(nums)/2) - 1
    root = TreeNode(nums[cur])
    for i in range(0, cur):
        node = TreeNode(nums[i])
        root.left = node
    for i in range(cur, len(nums)):
        node = TreeNode(nums[i])
        root.right = node

    return root

