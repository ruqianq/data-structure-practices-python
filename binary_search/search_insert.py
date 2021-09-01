# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return
# the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.
from typing import List

from binary_search.basic import get_mid_lower


def search_insert(nums: List[int], target: int) -> int:
    lo, hi = 0, len(nums)

    while lo < hi:
        mid = get_mid_lower(lo, hi)
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            lo = mid + 1
        else:
            hi = mid

    return lo

