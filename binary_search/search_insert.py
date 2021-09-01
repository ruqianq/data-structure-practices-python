# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.
from typing import List


def search_insert(nums: List[int], target: int) -> int:
    mid = len(nums)//2
    found = False
    if target == nums[mid]:
        return mid
    elif target > nums[mid]:

        while found is False and mid < len(nums) - 1:
            mid += 1
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                found = True
        if found is True:
            return mid
        else:
            return len(nums)

    else:
        while found is False and mid >= 0:
            mid -= 1
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                found = True
        if found is True:
            return mid + 1
        else:
            return 0

