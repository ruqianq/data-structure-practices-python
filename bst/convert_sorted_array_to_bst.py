# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
#
# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
#
from typing import List, Optional
from .treenode import TreeNode


def sorted_array_to_bst(nums: List[int]) -> Optional[TreeNode]:
    if not nums:
        return None

    mid = len(nums) // 2

    root = TreeNode(nums[mid])
    root.left = sorted_array_to_bst(nums[:mid])
    root.right = sorted_array_to_bst(nums[mid+1:])

    return root

